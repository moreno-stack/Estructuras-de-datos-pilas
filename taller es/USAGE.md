# 📖 Guía de Uso - Pipeline CI/CD Simulator

## Tabla de Contenidos
1. [Conceptos Básicos](#conceptos-básicos)
2. [Crear un Pipeline](#crear-un-pipeline)
3. [Ejecutar un Pipeline](#ejecutar-un-pipeline)
4. [Analizar Resultados](#analizar-resultados)
5. [Ejemplos de Uso](#ejemplos-de-uso)

---

## Conceptos Básicos

### ¿Qué es un Pipeline CI/CD?

Un **Pipeline CI/CD** es un flujo automatizado con tres fases:

1. **Integración (CI)**: Compilar y probar código automáticamente
2. **Despliegue (CD)**: Publicar la aplicación automáticamente

### Componentes

- **Pipeline**: Flujo completo de automatización
- **Job**: Grupo de pasos relacionados
- **Step**: Comando individual a ejecutar

### Ejemplo Visual

```
Pipeline: "Desplegar Aplicación"
├── Job: "Compilar"
│   ├── Step: "Clonar código"
│   ├── Step: "Instalar dependencias"
│   └── Step: "Compilar"
├── Job: "Probar"
│   ├── Step: "Ejecutar unit tests"
│   └── Step: "Ejecutar integration tests"
└── Job: "Desplegar"
    ├── Step: "Crear imagen Docker"
    └── Step: "Publicar en producción"
```

---

## Crear un Pipeline

### Opción 1: Usar un Template

1. Abre **"📦 Crear Pipeline"**
2. En "Usar Template", selecciona:
   - `básico` - Pipeline simple (compilar + probar)
   - `completo` - Pipeline real (compilar + probar + desplegar)
3. Personaliza el nombre del pipeline y proyecto
4. Haz clic en **"➕ Crear Pipeline"**

### Opción 2: Crear Manualmente

1. Abre **"📦 Crear Pipeline"**
2. Selecciona "Personalizado"
3. Ingresa:
   - **Nombre del Pipeline**: Ej. "Mi Aplicación"
   - **Nombre del Proyecto**: Ej. "webapp-frontend"
4. Haz clic en **"➕ Crear Pipeline"**
5. En "Editor de Pipeline":
   - Agrega un Job con un nombre descriptivo
   - Dentro de cada Job, agrega Steps con comandos

### Ejemplo de Creación Manual

```
Pipeline: "Deploy Web App"
  → Job: "Compilar"
     → Step "npm install" | Comando: npm install
     → Step "npm build" | Comando: npm run build

  → Job: "Probar"
     → Step "test" | Comando: npm test
```

---

## Ejecutar un Pipeline

### Pasos

1. Abre **"▶️ Ejecutar"**
2. Selecciona un pipeline de la lista
3. Revisa la información del pipeline
4. Haz clic en **"🚀 EJECUTAR PIPELINE"**
5. Observa el progreso en tiempo real

### Durante la Ejecución

- ✅ Verás el progreso de cada job
- 📋 Se mostrará el output de cada comando
- ⏱️ Se registrará el tiempo de ejecución

### Después de la Ejecución

- 📊 Estado general (Exitoso/Fallido)
- ⏱️ Duración total
- 📈 Porcentaje de éxito
- 🔍 Detalles de cada job y paso

---

## Analizar Resultados

### Dashboard de Estadísticas

Abre **"📊 Estadísticas"** para ver:

- **Métricas Generales**:
  - Total de pipelines ejecutados
  - Total de jobs ejecutados
  - Pipelines exitosos
  - Pipelines fallidos

- **Tabla de Histórico**: Lista todos los pipelines con detalles

- **Gráficos**:
  - Distribución de estados (pastel)
  - Duración promedio de ejecución

### Historial Detallado

Abre **"📜 Historial"** para:
- Ver todas las ejecuciones previas
- Expandir cada ejecución para ver detalles
- Revisar el output de cada job

---

## Ejemplos de Uso

### Ejemplo 1: Pipeline Básico de Node.js

```
Nombre: "Build React App"
Proyecto: "react-dashboard"

Job: "Compilación"
  - Step: "install"
    Comando: npm install
  
  - Step: "build"
    Comando: npm run build

Job: "Testing"
  - Step: "test"
    Comando: npm test
```

### Ejemplo 2: Pipeline Python

```
Nombre: "Deploy Python API"
Proyecto: "fastapi-backend"

Job: "Setup"
  - Step: "install"
    Comando: pip install -r requirements.txt

Job: "Quality"
  - Step: "lint"
    Comando: pylint app/
  
  - Step: "test"
    Comando: pytest tests/

Job: "Deploy"
  - Step: "build"
    Comando: docker build -t api .
  
  - Step: "push"
    Comando: docker push myregistry/api
```

### Ejemplo 3: Pipeline Docker

```
Nombre: "Docker CI/CD"
Proyecto: "microservices"

Job: "Build Images"
  - Step: "build-api"
    Comando: docker build -f Dockerfile.api -t api:latest .
  
  - Step: "build-web"
    Comando: docker build -f Dockerfile.web -t web:latest .

Job: "Push to Registry"
  - Step: "push-api"
    Comando: docker push myregistry/api:latest
  
  - Step: "push-web"
    Comando: docker push myregistry/web:latest

Job: "Deploy"
  - Step: "deploy-staging"
    Comando: kubectl apply -f k8s/staging/
  
  - Step: "deploy-prod"
    Comando: kubectl apply -f k8s/production/
```

---

## Consejos Prácticos

### ✅ Buenas Prácticas

1. **Nombres Descriptivos**: Usa nombres claros para pipelines, jobs y steps
2. **Pasos Pequeños**: Divide tareas complejas en pasos simples
3. **Order Lógico**: Organiza jobs en orden lógico (compile → test → deploy)
4. **Manejo de Errores**: Los pasos fallidos detienen el job automáticamente

### 🚀 Optimización

1. **Reutilizar Templates**: Usa templates para pipelines similares
2. **Monitoreo**: Revisa estadísticas regularmente
3. **Historial**: Consulta ejecuciones anteriores para mejorar

### 🔍 Debugging

1. Si un paso falla, revisa el output de error
2. Verifica que los comandos sean correctos
3. Asegúrate de que existan las herramientas necesarias

---

## Atajos Útiles

| Acción | Ubicación |
|--------|-----------|
| Ver inicio | Menú lateral → "🏠 Inicio" |
| Crear pipeline | Menú lateral → "📦 Crear Pipeline" |
| Ejecutar | Menú lateral → "▶️ Ejecutar" |
| Estadísticas | Menú lateral → "📊 Estadísticas" |
| Historial | Menú lateral → "📜 Historial" |

---

## Soporte

¿Problemas? Consulta:
- [INSTALL.md](INSTALL.md) - Problemas de instalación
- [README.md](README.md) - Documentación general

---

**¡Disfruta construyendo tus pipelines CI/CD! 🚀**
