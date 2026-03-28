"""
Módulo principal de gestión de pipelines CI/CD
"""
import json
from typing import List, Optional
from .models import Pipeline, Job, Step, JobStatus, StepStatus
from .executor import PipelineExecutor


class PipelineManager:
    """Gestor de pipelines CI/CD"""
    
    def __init__(self):
        """Inicializa el gestor"""
        self.pipelines: List[Pipeline] = []
        self.executor = PipelineExecutor()
    
    def create_pipeline(self, name: str, project_name: str) -> Pipeline:
        """
        Crea un nuevo pipeline
        
        Args:
            name: Nombre del pipeline
            project_name: Nombre del proyecto
            
        Returns:
            Pipeline creado
        """
        pipeline = Pipeline(name=name, project_name=project_name)
        self.pipelines.append(pipeline)
        return pipeline
    
    def add_job(self, pipeline: Pipeline, job_name: str) -> Job:
        """
        Agrega un job a un pipeline
        
        Args:
            pipeline: Pipeline al que agregar el job
            job_name: Nombre del job
            
        Returns:
            Job creado
        """
        job = Job(name=job_name, steps=[])
        pipeline.jobs.append(job)
        return job
    
    def add_step(self, job: Job, step_name: str, command: str) -> Step:
        """
        Agrega un paso a un job
        
        Args:
            job: Job al que agregar el paso
            step_name: Nombre del paso
            command: Comando a ejecutar
            
        Returns:
            Step creado
        """
        step = Step(name=step_name, command=command)
        job.steps.append(step)
        return step
    
    def execute_pipeline(self, pipeline: Pipeline, on_progress=None) -> Pipeline:
        """
        Ejecuta un pipeline
        
        Args:
            pipeline: Pipeline a ejecutar
            on_progress: Callback para progreso
            
        Returns:
            Pipeline ejecutado
        """
        executor = PipelineExecutor(on_progress=on_progress)
        return executor.execute_pipeline(pipeline)
    
    def get_pipeline_stats(self, pipeline: Pipeline) -> dict:
        """
        Obtiene estadísticas del pipeline
        
        Args:
            pipeline: Pipeline a analizar
            
        Returns:
            Diccionario con estadísticas
        """
        total_jobs = len(pipeline.jobs)
        successful_jobs = sum(1 for job in pipeline.jobs if job.status == JobStatus.SUCCESS)
        failed_jobs = sum(1 for job in pipeline.jobs if job.status == JobStatus.FAILED)
        total_steps = sum(len(job.steps) for job in pipeline.jobs)
        
        return {
            "total_jobs": total_jobs,
            "successful_jobs": successful_jobs,
            "failed_jobs": failed_jobs,
            "total_steps": total_steps,
            "success_percentage": pipeline.get_success_percentage(),
            "total_duration": pipeline.get_total_duration(),
            "status": pipeline.status.value
        }


# Templates de pipelines predefinidos
PIPELINE_TEMPLATES = {
    "básico": {
        "jobs": [
            {
                "name": "compilar",
                "steps": [
                    {"name": "verificar código", "command": "echo 'Compilando...'"}
                ]
            },
            {
                "name": "probar",
                "steps": [
                    {"name": "correr tests", "command": "echo 'Ejecutando tests...'"}
                ]
            }
        ]
    },
    "completo": {
        "jobs": [
            {
                "name": "compilar",
                "steps": [
                    {"name": "instalar dependencias", "command": "echo 'Instalando dependencias...'"},
                    {"name": "compilar", "command": "echo 'Compilando código...'"}
                ]
            },
            {
                "name": "probar",
                "steps": [
                    {"name": "unit tests", "command": "echo 'Ejecutando unit tests...'"},
                    {"name": "integration tests", "command": "echo 'Ejecutando integration tests...'"}
                ]
            },
            {
                "name": "desplegar",
                "steps": [
                    {"name": "crear imagen", "command": "echo 'Creando imagen Docker...'"},
                    {"name": "publicar", "command": "echo 'Publicando a registro..."}
                ]
            }
        ]
    }
}
