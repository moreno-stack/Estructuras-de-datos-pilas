# 🚀 Guía de Instalación - Pipeline CI/CD Simulator

## Requisitos Previos

- **Python 3.8 o superior** - [Descargar](https://www.python.org/downloads/)
- **pip** - Gestor de paquetes (incluido con Python)
- **Git** (opcional) - Para clonar el repositorio

## Pasos de Instalación

### 1️⃣ Descargar el Proyecto

#### Opción A: Con Git
```bash
git clone <url-del-repositorio>
cd "taller es"
```

#### Opción B: Descargar ZIP
- Descarga el archivo ZIP del proyecto
- Extrae la carpeta
- Abre terminal en la carpeta extraída

### 2️⃣ Crear Entorno Virtual (Recomendado)

Un entorno virtual aisla las dependencias del proyecto.

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Verás `(venv)` al inicio de la terminal cuando esté activado.

### 3️⃣ Instalar Dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Esto instalará:
- ✅ Streamlit (interfaz gráfica)
- ✅ Pandas (análisis de datos)
- ✅ Plotly (gráficos)
- ✅ Y más...

## 🚀 Ejecutar la Aplicación

Con el entorno virtual activado:

```bash
streamlit run app/frontend/streamlit_app.py
```

O usando el archivo main.py:

```bash
python main.py
```

La aplicación se abrirá automáticamente en:

```
http://localhost:8501
```

## ✅ Verificar Instalación

Para verificar que todo está correctamente instalado:

```bash
python -c "import streamlit; print(f'Streamlit {streamlit.__version__} instalado')"
```

## 📋 Estructura de Carpetas

```
taller es/
├── README.md              # Documentación principal
├── INSTALL.md            # Este archivo
├── requirements.txt      # Dependencias del proyecto
├── config.ini           # Configuración
├── main.py              # Punto de entrada
└── app/
    ├── frontend/        # Interfaz gráfica (Streamlit)
    │   └── streamlit_app.py
    ├── backend/         # Lógica del simulador (Python)
    │   ├── models.py    # Modelos de datos
    │   ├── pipeline.py  # Gestor de pipelines
    │   └── executor.py  # Ejecutor de pipelines
    └── utils/          # Funciones auxiliares
        └── helpers.py
```

## 🆘 Troubleshooting

### Problema: "Python no existe" o "comando no reconocido"

**Solución:** 
- En Windows, intenta con `py` en lugar de `python`
- `py -m venv venv`

### Problema: "module not found" después de instalar dependencias

**Solución:**
- Verifica que el entorno virtual esté activado
- Vuelve a ejecutar `pip install -r requirements.txt`

### Problema: Puerto 8501 ya está en uso

**Solución:** Especifica un puerto diferente
```bash
streamlit run app/frontend/streamlit_app.py --server.port=8502
```

### Problema: No se abre el navegador automáticamente

**Solución:** Abre manualmente `http://localhost:8501` en tu navegador

## 🎓 Primeros Pasos

1. Inicia la aplicación
2. Ve a la sección "📦 Crear Pipeline"
3. Selecciona un template o crea uno personalizado
4. Agrega jobs y pasos
5. Ve a "▶️ Ejecutar" y haz clic en "🚀 EJECUTAR PIPELINE"
6. Visualiza los resultados en real time

## 📚 Más Información

- [Documentación Streamlit](https://docs.streamlit.io/)
- [Documentación Python](https://docs.python.org/3/)

## 💡 Notas Importantes

- El taller es **individual**
- Frontend: **Streamlit**
- Backend: **Python**
- No se requiere configuración de base de datos

¡Listo para usar! ✨
