"""
Punto de entrada principal de la aplicación
Pipeline de Integración y Despliegue (Simulador CI/CD)
"""
import subprocess
import sys


def main():
    """Inicia la aplicación Streamlit"""
    print("=" * 60)
    print("🚀 Pipeline CI/CD Simulator")
    print("=" * 60)
    print("\nIniciando Streamlit...")
    print("La aplicación se abrirá en: http://localhost:8501\n")
    
    # Ejecutar Streamlit
    subprocess.run([
        sys.executable, "-m", "streamlit", "run",
        "app/frontend/streamlit_app.py"
    ])


if __name__ == "__main__":
    main()
