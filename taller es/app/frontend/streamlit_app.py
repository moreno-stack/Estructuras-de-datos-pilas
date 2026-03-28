"""
Aplicación Frontend con Streamlit
Pipeline de Integración y Despliegue (Simulador CI/CD)
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import sys
from pathlib import Path

# Agregar la ruta del proyecto
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.backend.pipeline import PipelineManager, PIPELINE_TEMPLATES
from app.backend.models import JobStatus, StepStatus


# Configuración de la página
st.set_page_config(
    page_title="CI/CD Pipeline Simulator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5em;
        color: #FF6B35;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 1.5em;
        color: #004E89;
        margin-bottom: 20px;
    }
    .success {
        color: #27AE60;
        font-weight: bold;
    }
    .failed {
        color: #E74C3C;
        font-weight: bold;
    }
    .running {
        color: #F39C12;
        font-weight: bold;
    }
    .stat-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #F8F9FA;
        margin: 10px 0;
        border-left: 5px solid #FF6B35;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar sesión
if 'pipeline_manager' not in st.session_state:
    st.session_state.pipeline_manager = PipelineManager()
    st.session_state.current_pipeline = None
    st.session_state.execution_log = []

# Cabecera principal
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown('<div class="main-header">🚀 Pipeline CI/CD Simulator</div>', unsafe_allow_html=True)
    st.markdown('**Pipeline de Integración y Despliegue (Simulador CI/CD)**')
with col2:
    st.info("📌 Taller Individual - Marzo 2026")

st.divider()

# Sidebar - Navegación
with st.sidebar:
    st.markdown("### ⚙️ Control del Pipeline")
    
    menu = st.radio(
        "Selecciona una opción:",
        ["🏠 Inicio", "📦 Crear Pipeline", "▶️ Ejecutar", "📊 Estadísticas", "📜 Historial"]
    )

# ========== PÁGINA: INICIO ==========
if menu == "🏠 Inicio":
    st.markdown('<div class="subheader">Bienvenido al Simulador CI/CD</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📋 ¿Qué es un Pipeline CI/CD?
        
        Un **Pipeline CI/CD** es una serie de pasos automatizados que:
        
        1. **Compilar** 📦 - Construye el código
        2. **Probar** 🧪 - Ejecuta tests automáticamente
        3. **Desplegar** 🚀 - Publica la aplicación
        
        Similar a **GitHub Actions** o **Jenkins**
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Características
        
        ✅ Crear pipelines personalizados  
        ✅ Definir jobs y pasos  
        ✅ Ejecutar automáticamente  
        ✅ Ver resultados en tiempo real  
        ✅ Analizar estadísticas  
        
        ### 🛠️ Stack Tecnológico
        - **Frontend**: Streamlit
        - **Backend**: Python
        """)
    
    st.divider()
    
    # Cards de estadísticas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Pipelines", len(st.session_state.pipeline_manager.pipelines))
    
    with col2:
        total_execuciones = sum(1 for p in st.session_state.pipeline_manager.pipelines if p.started_at)
        st.metric("Ejecuciones", total_execuciones)
    
    with col3:
        exitosas = sum(1 for p in st.session_state.pipeline_manager.pipelines if p.status == JobStatus.SUCCESS)
        st.metric("Exitosas", exitosas)
    
    with col4:
        fallidas = sum(1 for p in st.session_state.pipeline_manager.pipelines if p.status == JobStatus.FAILED)
        st.metric("Fallidas", fallidas)

# ========== PÁGINA: CREAR PIPELINE ==========
elif menu == "📦 Crear Pipeline":
    st.markdown('<div class="subheader">Crear Nuevo Pipeline</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Usar Template")
        template_choice = st.selectbox(
            "Selecciona un template:",
            ["Personalizado"] + list(PIPELINE_TEMPLATES.keys())
        )
    
    with col2:
        st.subheader("O crear manual")
        col_name, col_proj = st.columns(2)
        with col_name:
            pipeline_name = st.text_input("Nombre del Pipeline", value="Mi Pipeline")
        with col_proj:
            project_name = st.text_input("Nombre del Proyecto", value="Mi Proyecto")
    
    st.divider()
    
    if st.button("➕ Crear Pipeline", type="primary", use_container_width=True):
        pipeline = st.session_state.pipeline_manager.create_pipeline(pipeline_name, project_name)
        st.session_state.current_pipeline = pipeline
        
        if template_choice != "Personalizado":
            template = PIPELINE_TEMPLATES[template_choice]
            for job_data in template.get("jobs", []):
                job = st.session_state.pipeline_manager.add_job(pipeline, job_data["name"])
                for step_data in job_data.get("steps", []):
                    st.session_state.pipeline_manager.add_step(job, step_data["name"], step_data["command"])
        
        st.success(f"✅ Pipeline '{pipeline_name}' creado exitosamente")
        st.rerun()
    
    st.divider()
    st.subheader("📝 Editor de Pipeline")
    
    if st.session_state.current_pipeline:
        pipeline = st.session_state.current_pipeline
        st.info(f"Pipeline actual: **{pipeline.name}** (Proyecto: {pipeline.project_name})")
        
        # Agregar Jobs
        st.markdown("### ➕ Agregar Jobs")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            new_job_name = st.text_input("Nombre del Job", key="job_name")
        with col2:
            if st.button("Agregar Job", use_container_width=True):
                if new_job_name:
                    st.session_state.pipeline_manager.add_job(pipeline, new_job_name)
                    st.success(f"Job '{new_job_name}' agregado")
                    st.rerun()
        
        # Listar Jobs y agregar Steps
        st.markdown("### 📋 Jobs del Pipeline")
        
        for i, job in enumerate(pipeline.jobs):
            with st.expander(f"Job: {job.name}", expanded=True):
                # Agregar pasos al job
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    step_name = st.text_input(f"Nombre del paso", key=f"step_name_{i}")
                with col2:
                    step_command = st.text_input(f"Comando", key=f"step_cmd_{i}")
                with col3:
                    if st.button("➕ Paso", key=f"add_step_{i}"):
                        if step_name and step_command:
                            st.session_state.pipeline_manager.add_step(job, step_name, step_command)
                            st.success(f"Paso '{step_name}' agregado")
                            st.rerun()
                
                # Listar pasos
                if job.steps:
                    st.markdown("**Pasos:**")
                    for j, step in enumerate(job.steps):
                        st.write(f"`{j+1}.` {step.name} → `{step.command}`")
                else:
                    st.info("No hay pasos agregados")

# ========== PÁGINA: EJECUTAR ==========
elif menu == "▶️ Ejecutar":
    st.markdown('<div class="subheader">Ejecutar Pipeline</div>', unsafe_allow_html=True)
    
    if not st.session_state.pipeline_manager.pipelines:
        st.warning("⚠️ No hay pipelines creados. Crea uno primero en la sección 'Crear Pipeline'")
    else:
        # Seleccionar pipeline
        pipeline_names = [p.name for p in st.session_state.pipeline_manager.pipelines]
        selected_pipeline_name = st.selectbox("Selecciona un pipeline:", pipeline_names)
        
        pipeline = next(p for p in st.session_state.pipeline_manager.pipelines if p.name == selected_pipeline_name)
        st.session_state.current_pipeline = pipeline
        
        # Información del pipeline
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"📦 Pipeline: **{pipeline.name}**")
        with col2:
            st.info(f"📂 Proyecto: **{pipeline.project_name}**")
        with col3:
            st.info(f"🎯 Jobs: **{len(pipeline.jobs)}**")
        
        st.divider()
        
        # Botón de ejecutación
        if st.button("🚀 EJECUTAR PIPELINE", type="primary", use_container_width=True):
            st.session_state.execution_log = []
            progress_placeholder = st.empty()
            log_placeholder = st.empty()
            
            def log_progress(message):
                st.session_state.execution_log.append(message)
                with log_placeholder.container():
                    st.code("\n".join(st.session_state.execution_log), language="bash")
            
            # Ejecutar pipeline
            pipeline = st.session_state.pipeline_manager.execute_pipeline(
                pipeline, 
                on_progress=log_progress
            )
            
            st.rerun()
        
        st.divider()
        
        # Mostrar resultados si hay ejecución
        if pipeline.started_at:
            st.markdown("### 📊 Resultados de Ejecución")
            
            # Estado general
            if pipeline.status == JobStatus.SUCCESS:
                st.success("✅ Pipeline ejecutado exitosamente", icon="✅")
            else:
                st.error("❌ Pipeline falló", icon="❌")
            
            # Información de ejecución
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Estado", pipeline.status.value.upper())
            with col2:
                st.metric("Duración", f"{pipeline.get_total_duration():.2f}s")
            with col3:
                st.metric("Éxito", f"{pipeline.get_success_percentage():.1f}%")
            
            st.divider()
            
            # Detalles de Jobs
            st.markdown("### 🔍 Detalles de Jobs")
            
            for job in pipeline.jobs:
                status_icon = "✅" if job.status == JobStatus.SUCCESS else "❌"
                with st.expander(f"{status_icon} {job.name}", expanded=True):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Estado:** {job.status.value}")
                    with col2:
                        st.write(f"**Duración:** {job.duration:.2f}s")
                    with col3:
                        st.write(f"**Pasos:** {len(job.steps)}")
                    
                    st.markdown("**Detalles de Pasos:**")
                    for step in job.steps:
                        if step.status == StepStatus.SUCCESS:
                            st.success(f"✅ {step.name} ({step.duration:.2f}s)")
                        else:
                            st.error(f"❌ {step.name}")
                            if step.error:
                                st.code(step.error, language="bash")

# ========== PÁGINA: ESTADÍSTICAS ==========
elif menu == "📊 Estadísticas":
    st.markdown('<div class="subheader">Estadísticas del Sistema</div>', unsafe_allow_html=True)
    
    pipelines = st.session_state.pipeline_manager.pipelines
    
    if not pipelines:
        st.info("No hay datos de pipelines para mostrar estadísticas")
    else:
        # Métricas generales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Pipelines", len(pipelines))
        
        with col2:
            total_jobs = sum(len(p.jobs) for p in pipelines)
            st.metric("Total Jobs", total_jobs)
        
        with col3:
            exitosos = sum(1 for p in pipelines if p.status == JobStatus.SUCCESS)
            st.metric("Pipelines Exitosos", exitosos)
        
        with col4:
            fallidos = sum(1 for p in pipelines if p.status == JobStatus.FAILED)
            st.metric("Pipelines Fallidos", fallidos)
        
        st.divider()
        
        # Tabla de pipelines
        st.markdown("### 📋 Historial de Pipelines")
        
        pipeline_data = []
        for p in pipelines:
            pipeline_data.append({
                "Nombre": p.name,
                "Proyecto": p.project_name,
                "Estado": p.status.value if p.started_at else "pendiente",
                "Jobs": len(p.jobs),
                "Duración (s)": f"{p.get_total_duration():.2f}" if p.started_at else "-",
                "Éxito (%)": f"{p.get_success_percentage():.1f}%" if p.started_at else "-"
            })
        
        df = pd.DataFrame(pipeline_data)
        st.dataframe(df, use_container_width=True)
        
        st.divider()
        
        # Gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📈 Distribución de Estados")
            estados = {"Exitosos": exitosos, "Fallidos": fallidos, "Pendientes": len(pipelines) - exitosos - fallidos}
            fig, ax = plt.subplots()
            ax.pie(estados.values(), labels=estados.keys(), autopct='%1.1f%%', colors=['#27AE60', '#E74C3C', '#95A5A6'])
            st.pyplot(fig)
        
        with col2:
            st.markdown("### ⏱️ Duración Promedio")
            executed = [p for p in pipelines if p.started_at]
            if executed:
                duraciones = [p.get_total_duration() for p in executed]
                promedio = sum(duraciones) / len(duraciones)
                st.metric("Duración Promedio", f"{promedio:.2f}s", delta=f"Min: {min(duraciones):.2f}s, Max: {max(duraciones):.2f}s")
            else:
                st.info("Sin datos de ejecución")

# ========== PÁGINA: HISTORIAL ==========
elif menu == "📜 Historial":
    st.markdown('<div class="subheader">Historial de Ejecuciones</div>', unsafe_allow_html=True)
    
    pipelines = st.session_state.pipeline_manager.pipelines
    
    if not pipelines:
        st.info("No hay pipelines en el historial")
    else:
        for pipeline in reversed(pipelines):
            if pipeline.started_at:
                status_emoji = "✅" if pipeline.status == JobStatus.SUCCESS else "❌"
                
                with st.expander(f"{status_emoji} {pipeline.name} - {pipeline.created_at.strftime('%Y-%m-%d %H:%M:%S')}"):
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.write(f"**Proyecto:** {pipeline.project_name}")
                    with col2:
                        st.write(f"**Estado:** {pipeline.status.value}")
                    with col3:
                        st.write(f"**Duración:** {pipeline.get_total_duration():.2f}s")
                    with col4:
                        st.write(f"**Éxito:** {pipeline.get_success_percentage():.1f}%")
                    
                    st.divider()
                    
                    # Detalles de jobs
                    for job in pipeline.jobs:
                        job_icon = "✅" if job.status == JobStatus.SUCCESS else "❌"
                        st.write(f"{job_icon} **{job.name}** - {job.status.value} ({job.duration:.2f}s)")

st.divider()

# Footer
st.markdown("""
    ---
    <div style="text-align: center; color: #7F8C8D; font-size: 0.9em;">
    <strong>Pipeline CI/CD Simulator</strong> | Taller Individual 2026 | 
    Frontend: Streamlit | Backend: Python
    </div>
""", unsafe_allow_html=True)
