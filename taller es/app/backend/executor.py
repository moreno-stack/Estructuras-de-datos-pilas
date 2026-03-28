"""
Ejecutor de pipelines CI/CD
"""
import subprocess
import time
from datetime import datetime
from typing import Callable, Optional
from .models import Pipeline, Job, Step, JobStatus, StepStatus


class PipelineExecutor:
    """Ejecuta pipelines CI/CD de forma simulada"""
    
    def __init__(self, on_progress: Optional[Callable] = None):
        """
        Inicializa el ejecutor
        
        Args:
            on_progress: Callback para reportar progreso (opcional)
        """
        self.on_progress = on_progress or (lambda msg: None)
    
    def execute_pipeline(self, pipeline: Pipeline) -> Pipeline:
        """
        Ejecuta un pipeline completo
        
        Args:
            pipeline: Pipeline a ejecutar
            
        Returns:
            Pipeline actualizado con resultados
        """
        pipeline.started_at = datetime.now()
        pipeline.status = JobStatus.RUNNING
        
        self.on_progress(f"Iniciando ejecución del pipeline: {pipeline.name}")
        
        for job in pipeline.jobs:
            self.execute_job(job)
        
        pipeline.finished_at = datetime.now()
        
        # Determinar estado final del pipeline
        all_success = all(job.status == JobStatus.SUCCESS for job in pipeline.jobs)
        pipeline.status = JobStatus.SUCCESS if all_success else JobStatus.FAILED
        
        duration = pipeline.get_total_duration()
        self.on_progress(f"Pipeline finalizado en {duration:.2f}s")
        
        return pipeline
    
    def execute_job(self, job: Job) -> Job:
        """
        Ejecuta un job con todos sus pasos
        
        Args:
            job: Job a ejecutar
            
        Returns:
            Job actualizado con resultados
        """
        job.status = JobStatus.RUNNING
        job.start_time = datetime.now()
        
        self.on_progress(f"  → Ejecutando job: {job.name}")
        
        for step in job.steps:
            self.execute_step(step)
            # Si un paso falla, el job falla
            if step.status == StepStatus.FAILED:
                job.status = JobStatus.FAILED
                break
        
        job.end_time = datetime.now()
        job.duration = (job.end_time - job.start_time).total_seconds()
        
        # Si todos los pasos fueron exitosos
        if job.status != JobStatus.FAILED:
            job.status = JobStatus.SUCCESS
        
        status_text = "✓" if job.status == JobStatus.SUCCESS else "✗"
        self.on_progress(f"    {status_text} Job {job.name}: {job.status}")
        
        return job
    
    def execute_step(self, step: Step) -> Step:
        """
        Ejecuta un paso individual
        
        Args:
            step: Paso a ejecutar
            
        Returns:
            Paso actualizado con resultados
        """
        step.status = StepStatus.RUNNING
        start_time = time.time()
        
        try:
            # Ejecutar comando
            result = subprocess.run(
                step.command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            step.output = result.stdout
            step.error = result.stderr
            step.duration = time.time() - start_time
            
            # Determinar si fue exitoso
            if result.returncode == 0:
                step.status = StepStatus.SUCCESS
                self.on_progress(f"      ✓ {step.name}")
            else:
                step.status = StepStatus.FAILED
                self.on_progress(f"      ✗ {step.name} - Error: {step.error[:100]}")
        
        except subprocess.TimeoutExpired:
            step.status = StepStatus.FAILED
            step.error = "Timeout: El comando tardó demasiado"
            step.duration = time.time() - start_time
            self.on_progress(f"      ✗ {step.name} - Timeout")
        
        except Exception as e:
            step.status = StepStatus.FAILED
            step.error = str(e)
            step.duration = time.time() - start_time
            self.on_progress(f"      ✗ {step.name} - Excepción: {str(e)}")
        
        return step
