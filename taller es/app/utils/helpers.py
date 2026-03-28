"""
Funciones auxiliares para el simulador CI/CD
"""
from datetime import datetime
from typing import List


def format_duration(seconds: float) -> str:
    """
    Formatea duración en segundos a texto legible
    
    Args:
        seconds: Duración en segundos
        
    Returns:
        String formateado (ej: "1h 30m 45s")
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")
    
    return " ".join(parts)


def format_datetime(dt: datetime) -> str:
    """
    Formatea un datetime a string legible
    
    Args:
        dt: Datetime a formatear
        
    Returns:
        String formateado
    """
    if dt is None:
        return "N/A"
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_status_color(status: str) -> str:
    """
    Retorna color basado en estado
    
    Args:
        status: Estado (success, failed, running, pending)
        
    Returns:
        Código de color
    """
    colors = {
        "exitoso": "#27AE60",
        "fallido": "#E74C3C",
        "ejecutando": "#F39C12",
        "pendiente": "#95A5A6"
    }
    return colors.get(status, "#95A5A6")


def create_sample_pipelines() -> List[dict]:
    """
    Crea pipelines de ejemplo
    
    Returns:
        List de pipelines de ejemplo
    """
    return [
        {
            "name": "Compilación Simple",
            "project": "webapp-frontend",
            "jobs": [
                {
                    "name": "build",
                    "steps": [
                        {"name": "checkout", "command": "echo 'Clonando repositorio'"},
                        {"name": "install", "command": "echo 'npm install'"},
                        {"name": "build", "command": "echo 'npm run build'"}
                    ]
                }
            ]
        },
        {
            "name": "CI/CD Completo",
            "project": "api-backend",
            "jobs": [
                {
                    "name": "test",
                    "steps": [
                        {"name": "setup", "command": "echo 'pip install -r requirements.txt'"},
                        {"name": "lint", "command": "echo 'pylint .'"},
                        {"name": "test", "command": "echo 'pytest'"}
                    ]
                },
                {
                    "name": "build",
                    "steps": [
                        {"name": "docker", "command": "echo 'docker build -t api .'"},
                        {"name": "push", "command": "echo 'docker push registry/api'"}
                    ]
                },
                {
                    "name": "deploy",
                    "steps": [
                        {"name": "staging", "command": "echo 'kubectl deploy staging'"},
                        {"name": "production", "command": "echo 'kubectl deploy production'"}
                    ]
                }
            ]
        }
    ]
