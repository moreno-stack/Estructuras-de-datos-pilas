# Pipeline de Integración y Despliegue (Simulador CI/CD)

![Taller](https://img.shields.io/badge/TALLER-Pipeline%20CI%2FCD-orange)
![Status](https://img.shields.io/badge/status-desarrollo-blue)

## 📋 Descripción del Proyecto

Una herramienta web interactiva de simulación de **CI/CD (Continuous Integration / Continuous Deployment)** que permite a los desarrolladores experimentar con pipelines de integración y despliegue automatizados.

Este proyecto construye el **core de una herramienta similar a GitHub Actions o Jenkins**, proporcionando una interfaz gráfica intuitiva para definir, ejecutar y monitorear pipelines de CI/CD.

## 🎯 Objetivo

Que todo equipo de desarrollo pueda experimentar con herramientas para:
- ✅ **Compilar** código de forma automatizada
- 🧪 **Probar** (testing) automáticamente
- 🚀 **Desplegar** versiones de forma automática

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|------------|-----------|
| **Frontend** | Streamlit (Python) |
| **Backend** | Python |
| **Base de Datos** | JSON/SQLite (opcional) |

## 📁 Estructura del Proyecto

```
taller es/
├── README.md
├── requirements.txt
├── main.py
├── app/
│   ├── __init__.py
│   ├── frontend/
│   │   ├── __init__.py
│   │   └── streamlit_app.py
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── pipeline.py
│   │   ├── executor.py
│   │   └── models.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
└── tests/
    └── test_pipeline.py
```

## 🚀 Instalación y Uso

### Requisitos
- Python 3.8+
- pip (gestor de paquetes)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd "taller es"
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   streamlit run app/frontend/streamlit_app.py
   ```

La aplicación se abrirá en: `http://localhost:8501`

## 💡 Características Principales

### 🔄 Simulador de Pipeline
- Crear pipelines personalizados
- Definir pasos (jobs) con comandos
- Ejecutar automáticamente
- Visualizar resultados en tiempo real

### 📊 Dashboard
- Historial de ejecuciones
- Estadísticas de éxito/fallo
- Logs detallados
- Visualización de pipelines

### 🎮 Interfaz Interactiva
- Diseño intuitivo y amigable
- Editor de configuración
- Simulación de ejecución
- Reportes y análisis

## 📝 Cómo Usar

1. **Crear un nuevo pipeline**
   - Ingresa el nombre del proyecto
   - Define los pasos (compilación, pruebas, despliegue)

2. **Configurar pasos**
   - Nombre del paso
   - Comando a ejecutar
   - Condiciones (opcional)

3. **Ejecutar pipeline**
   - Visualiza el progreso
   - Revisa logs en tiempo real
   - Analiza resultados

## 📌 Notas Importantes

- ⚠️ **NOTA 1**: Frontend con **Streamlit** | Backend con **Python**
- ⚠️ **NOTA 2**: El taller es **individual**

## 🔗 Contexto

Todo equipo de desarrollo necesita herramientas para compilar, probar y desplegar código de forma automatizada. Este simulador te permite experimentar con los conceptos de CI/CD sin necesidad de infraestructura real.

## 👨‍💻 Autor

**Taller Individual** - Marzo 2026

## 📄 Licencia

Este proyecto es de código abierto y libre para uso educativo.

---

**¿Necesitas ayuda?** Consulta la documentación o revisa los ejemplos en la carpeta `examples/`
