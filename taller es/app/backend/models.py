"""
Modelos de datos para el simulador CI/CD
"""
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class JobStatus(str, Enum):
    """Estados posibles de un job"""
    PENDING = "pendiente"
    RUNNING = "ejecutando"
    SUCCESS = "exitoso"
    FAILED = "fallido"
    CANCELLED = "cancelado"


class StepStatus(str, Enum):
    """Estados posibles de un paso"""
    PENDING = "pendiente"
    RUNNING = "ejecutando"
    SUCCESS = "exitoso"
    FAILED = "fallido"


@dataclass
class Step:
    """Representa un paso (comando) dentro de un job"""
    name: str
    command: str
    status: StepStatus = StepStatus.PENDING
    output: str = ""
    error: str = ""
    duration: float = 0.0


@dataclass
class Job:
    """Representa un job (tarea) dentro de un pipeline"""
    name: str
    steps: List[Step]
    status: JobStatus = JobStatus.PENDING
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration: float = 0.0


@dataclass
class Pipeline:
    """Representa un pipeline CI/CD completo"""
    name: str
    project_name: str
    jobs: List[Job] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    status: JobStatus = JobStatus.PENDING
    
    def get_total_duration(self) -> float:
        """Calcula el tiempo total de ejecución"""
        if self.started_at and self.finished_at:
            return (self.finished_at - self.started_at).total_seconds()
        return 0.0
    
    def get_success_percentage(self) -> float:
        """Calcula el porcentaje de éxito"""
        if not self.jobs:
            return 0.0
        successful = sum(1 for job in self.jobs if job.status == JobStatus.SUCCESS)
        return (successful / len(self.jobs)) * 100
