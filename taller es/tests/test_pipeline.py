"""
Pruebas unitarias para el simulador CI/CD
"""
import unittest
from app.backend.models import Pipeline, Job, Step, JobStatus, StepStatus
from app.backend.pipeline import PipelineManager


class TestPipelineModels(unittest.TestCase):
    """Pruebas para los modelos de Pipeline"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.pipeline = Pipeline(name="test-pipeline", project_name="test-project")
        self.job = Job(name="test-job", steps=[])
        self.step = Step(name="test-step", command="echo 'test'")
    
    def test_create_pipeline(self):
        """Prueba creación de pipeline"""
        self.assertEqual(self.pipeline.name, "test-pipeline")
        self.assertEqual(self.pipeline.project_name, "test-project")
        self.assertEqual(len(self.pipeline.jobs), 0)
    
    def test_create_job(self):
        """Prueba creación de job"""
        self.assertEqual(self.job.name, "test-job")
        self.assertEqual(self.job.status, JobStatus.PENDING)
    
    def test_create_step(self):
        """Prueba creación de paso"""
        self.assertEqual(self.step.name, "test-step")
        self.assertEqual(self.step.command, "echo 'test'")
        self.assertEqual(self.step.status, StepStatus.PENDING)
    
    def test_pipeline_success_percentage(self):
        """Prueba cálculo de porcentaje de éxito"""
        job1 = Job(name="job1", steps=[])
        job1.status = JobStatus.SUCCESS
        
        job2 = Job(name="job2", steps=[])
        job2.status = JobStatus.FAILED
        
        self.pipeline.jobs = [job1, job2]
        
        self.assertEqual(self.pipeline.get_success_percentage(), 50.0)


class TestPipelineManager(unittest.TestCase):
    """Pruebas para el gestor de pipelines"""
    
    def setUp(self):
        """Configuración inicial"""
        self.manager = PipelineManager()
    
    def test_create_pipeline(self):
        """Prueba creación de pipeline mediante manager"""
        pipeline = self.manager.create_pipeline("test", "project")
        
        self.assertEqual(len(self.manager.pipelines), 1)
        self.assertEqual(pipeline.name, "test")
    
    def test_add_job_to_pipeline(self):
        """Prueba agregar job a pipeline"""
        pipeline = self.manager.create_pipeline("test", "project")
        job = self.manager.add_job(pipeline, "test-job")
        
        self.assertEqual(len(pipeline.jobs), 1)
        self.assertEqual(job.name, "test-job")
    
    def test_add_step_to_job(self):
        """Prueba agregar paso a job"""
        pipeline = self.manager.create_pipeline("test", "project")
        job = self.manager.add_job(pipeline, "test-job")
        step = self.manager.add_step(job, "test-step", "echo 'test'")
        
        self.assertEqual(len(job.steps), 1)
        self.assertEqual(step.command, "echo 'test'")
    
    def test_get_pipeline_stats(self):
        """Prueba obtención de estadísticas"""
        pipeline = self.manager.create_pipeline("test", "project")
        job = self.manager.add_job(pipeline, "test-job")
        self.manager.add_step(job, "test-step", "echo 'test'")
        
        stats = self.manager.get_pipeline_stats(pipeline)
        
        self.assertEqual(stats["total_jobs"], 1)
        self.assertEqual(stats["total_steps"], 1)


if __name__ == "__main__":
    unittest.main()
