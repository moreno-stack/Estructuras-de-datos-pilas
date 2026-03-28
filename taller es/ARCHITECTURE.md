# 🏗️ Arquitectura del Proyecto

## Visión General

El **Pipeline CI/CD Simulator** es una aplicación Web que simula el funcionamiento de herramientas como GitHub Actions o Jenkins. Está construida con una arquitectura cliente-servidor clara y modular.

## Estructura General

```
┌─────────────────────────────────────────────────────┐
│           Frontend (Streamlit)                       │
│  ┌──────────────────────────────────────────────┐   │
│  │  Interfaz Gráfica Interactiva                │   │
│  │  - Dashboard                                  │   │
│  │  - Editor de Pipelines                        │   │
│  │  - Visualizador de Ejecuciones               │   │
│  │  - Estadísticas                              │   │
│  └──────────────────────────────────────────────┘   │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │   Backend (Python)   │
        ├──────────────────────┤
│  - PipelineManager        │
│  - PipelineExecutor       │
│  - Models                 │
│  - Utils                  │
        └──────────────────────┘
```

## Componentes Principales

### 1. Frontend (`app/frontend/`)

**Archivo**: `streamlit_app.py`

Responsable de:
- ✅ Interfaz gráfica con Streamlit
- ✅ Navegación entre secciones
- ✅ Entrada de datos del usuario
- ✅ Visualización de resultados
- ✅ Gráficos y estadísticas

**Secciones**:
- 🏠 **Inicio**: Bienvenida y estadísticas generales
- 📦 **Crear Pipeline**: Editor visual de pipelines
- ▶️ **Ejecutar**: Ejecución y monitoreo
- 📊 **Estadísticas**: Análisis de datos
- 📜 **Historial**: Registro de ejecuciones

### 2. Backend (`app/backend/`)

#### `models.py`
Define las estructuras de datos:
- `Step`: Un comando individual
- `Job`: Un grupo de pasos
- `Pipeline`: Flujo completo
- Enumeraciones de estados

#### `pipeline.py`
Gestión de pipelines:
- `PipelineManager`: Crea y gestiona pipelines
- `PIPELINE_TEMPLATES`: Templates predefinidos

#### `executor.py`
Ejecución de pipelines:
- `PipelineExecutor`: Ejecuta pasos y jobs
- Manejo de procesos
- Captura de output
- Registro de tiempos

### 3. Utilidades (`app/utils/`)

**Archivo**: `helpers.py`

Funciones auxiliares:
- Formateo de fechas
- Formateo de duraciones
- Códigos de color
- Generador de ejemplos

## Flujo de Datos

### Crear un Pipeline

```
Usuario
   ↓
Frontend (Streamlit)
   ↓ Input del usuario
Backend (PipelineManager)
   ↓ Crea objetos
Pipeline + Jobs + Steps
   ↓ Almacena en sesión
Interfaz se actualiza
```

### Ejecutar un Pipeline

```
Usuario → "EJECUTAR"
   ↓
Frontend → PipelineExecutor
   ↓
Para cada Job:
   ├─ Actualiza estado a RUNNING
   ├─ Para cada Step:
   │  ├─ Execute comando
   │  ├─ Captura output
   │  ├─ Registra tiempo
   │  └─ Actualiza estado
   └─ Reporta progreso
   ↓
Pipeline completo
   ↓
Frontend actualiza visualización
```

## Gestión del Estado

### Streamlit Session State

```python
st.session_state = {
    'pipeline_manager': PipelineManager(),
    'current_pipeline': Pipeline,
    'execution_log': []
}
```

**Razón**: Streamlit reeje la aplicación en cada interacción. El session state persiste datos entre actualizaciones.

## Patrones de Diseño

### 1. **Manager Pattern**
`PipelineManager` centraliza la creación y gestión de pipelines.

```python
manager = PipelineManager()
pipeline = manager.create_pipeline("name", "project")
manager.execute_pipeline(pipeline)
```

### 2. **Executor Pattern**
`PipelineExecutor` maneja la ejecución separado de la gestión.

```python
executor = PipelineExecutor(on_progress=callback)
executor.execute_pipeline(pipeline)
```

### 3. **Model Objects**
Objetos de datos (`Pipeline`, `Job`, `Step`) encapsulan información.

## Ciclo de Vida de la Aplicación

```
1. INICIALIZACIÓN
   └─ Streamlit carga streamlit_app.py
   └─ Inicializa session_state
   └─ Renderiza UI

2. INTERACCIÓN
   └─ Usuario interactúa con UI
   └─ Streamlit reeje la aplicación
   └─ Se ejecuta el código nuevamente
   └─ Session state persiste

3. EJECUCIÓN
   └─ Usuario ejecuta pipeline
   └─ Backend procesa comando
   └─ Callback actualiza UI
   └─ Resultados se muestran

4. ANÁLISIS
   └─ Usuario visualiza estadísticas
   └─ Historial se consulta
   └─ Datos se grafican
```

## Tecnologías Utilizadas

| Componente | Tecnología | Propósito |
|-----------|-----------|----------|
| Frontend | Streamlit | UI interactiva |
| Backend | Python | Lógica de negocio |
| Ejecución | subprocess | Ejecutar comandos |
| Análisis de datos | Pandas | Tablas y estadísticas |
| Visualización | Plotly/Matplotlib | Gráficos |

## Directorios y Archivos

```
taller es/
├── main.py                    # Punto de entrada
├── requirements.txt          # Dependencias
├── README.md                 # Documentación principal
├── INSTALL.md               # Guía de instalación
├── USAGE.md                 # Guía de uso
├── ARCHITECTURE.md          # Este archivo
├── LICENSE.md               # Licencia
└── app/
    ├── __init__.py
    ├── frontend/
    │   ├── __init__.py
    │   └── streamlit_app.py  # Aplicación principal
    ├── backend/
    │   ├── __init__.py
    │   ├── models.py         # Estructuras de datos
    │   ├── pipeline.py       # Gestión
    │   └── executor.py       # Ejecución
    └── utils/
        ├── __init__.py
        └── helpers.py        # Utilidades
└── tests/
    └── test_pipeline.py     # Pruebas unitarias
```

## Extensibilidad

El diseño permite fáciles extensiones:

### Agregar un Nuevo Job Type
1. Extender `Job` en `models.py`
2. Implementar lógica en `executor.py`

### Agregar Persistencia
1. Implementar `DatabaseManager`
2. Guardar pipelines en base de datos
3. Integrar con `PipelineManager`

### Agregar Webhooks
1. Crear `WebhookManager`
2. Llamar en puntos de ejecución
3. Integrar con `PipelineExecutor`

## Consideraciones de Rendimiento

- ✅ Session state evita recalculos innecesarios
- ✅ Callbacks actualizan UI sin bloqueos
- ✅ Subprocess maneja comandos de forma aislada
- ✅ Timeout de 30s previene comandos eternos

## Seguridad

- ⚠️ Los comandos se ejecutan con permisos del usuario
- ⚠️ No hay validación de entrada (para desarrollo)
- ⚠️ Los logs pueden contener información sensible

Para producción, se recomienda:
- Validar entrada de usuarios
- Usar entornos aislados (Docker)
- Implementar autenticación
- Encriptar datos sensibles

---

**Última actualización**: Marzo 2026
