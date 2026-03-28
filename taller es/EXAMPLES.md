# 📚 Ejemplos de Pipelines

Una colección de pipelines listos para usar como referencia.

## 1. Pipeline Node.js Básico

**Caso de Uso**: Compilar y probar una aplicación Node.js

### Configuración

```
Nombre Pipeline: "Node.js Build"
Proyecto: "nodejs-app"

Job 1: "Build"
  ├─ Step: "Install Dependencies"
  │  └─ Comando: npm install
  │
  └─ Step: "Build Project"
     └─ Comando: npm run build

Job 2: "Test"
  ├─ Step: "Run Tests"
  │  └─ Comando: npm test
  │
  └─ Step: "Coverage"
     └─ Comando: npm run coverage
```

### Output Esperado

```
✅ Node.js Build: exitoso (5.23s)
  ├─ Install Dependencies (1.45s)
  └─ Build Project (3.78s)

✅ Test: exitoso (8.15s)
  ├─ Run Tests (6.20s)
  └─ Coverage (1.95s)
```

---

## 2. Pipeline Python Django

**Caso de Uso**: Desplegar una aplicación Django

### Configuración

```
Nombre Pipeline: "Django Deploy"
Proyecto: "django-backend"

Job 1: "Setup"
  ├─ Step: "Install Dependencies"
  │  └─ Comando: pip install -r requirements.txt
  │
  ├─ Step: "Migrate Database"
  │  └─ Comando: python manage.py migrate
  │
  └─ Step: "Collect Static"
     └─ Comando: python manage.py collectstatic

Job 2: "Quality"
  ├─ Step: "Lint Code"
  │  └─ Comando: pylint app/
  │
  ├─ Step: "Format Check"
  │  └─ Comando: black --check .
  │
  └─ Step: "Run Tests"
     └─ Comando: pytest tests/

Job 3: "Deploy"
  └─ Step: "Deploy to Server"
     └─ Comando: docker build -t django-app . && docker push registry/django-app
```

---

## 3. Pipeline Docker Multi-Stage

**Caso de Uso**: Compilar, probar y publicar imagen Docker

### Configuración

```
Nombre Pipeline: "Docker CI/CD"
Proyecto: "microservice-api"

Job 1: "Build"
  └─ Step: "Build Docker Image"
     └─ Comando: docker build -t myapp:latest .

Job 2: "Test"
  ├─ Step: "Run Unit Tests"
  │  └─ Comando: docker run myapp:latest npm test
  │
  └─ Step: "Run Integration Tests"
     └─ Comando: docker run myapp:latest npm run integration-test

Job 3: "Push"
  ├─ Step: "Login to Registry"
  │  └─ Comando: docker login -u user -p pass
  │
  └─ Step: "Push Image"
     └─ Comando: docker push myregistry/myapp:latest

Job 4: "Deploy"
  ├─ Step: "Deploy to Staging"
  │  └─ Comando: kubectl set image deployment/myapp-staging myapp=myregistry/myapp:latest
  │
  └─ Step: "Deploy to Production"
     └─ Comando: kubectl set image deployment/myapp-prod myapp=myregistry/myapp:latest
```

---

## 4. Pipeline Frontend React

**Caso de Uso**: Compilar, probar y desplegar aplicación React

### Configuración

```
Nombre Pipeline: "React Deploy"
Proyecto: "react-dashboard"

Job 1: "Build"
  ├─ Step: "Install Packages"
  │  └─ Comando: npm install
  │
  ├─ Step: "Build Production"
  │  └─ Comando: npm run build
  │
  └─ Step: "Analyze Bundle"
     └─ Comando: npm run analyze

Job 2: "Test"
  ├─ Step: "Unit Tests"
  │  └─ Comando: npm test -- --coverage
  │
  └─ Step: "E2E Tests"
     └─ Comando: npm run cypress:run

Job 3: "Deploy"
  ├─ Step: "Upload to S3"
  │  └─ Comando: aws s3 sync build/ s3://mybucket/
  │
  └─ Step: "Invalidate CloudFront"
     └─ Comando: aws cloudfront create-invalidation --distribution-id E123456 --paths "/*"
```

---

## 5. Pipeline Multi-Lenguaje

**Caso de Uso**: Proyecto con múltiples componentes en diferentes lenguajes

### Configuración

```
Nombre Pipeline: "Full Stack Deploy"
Proyecto: "fullstack-app"

Job 1: "Build Backend"
  ├─ Step: "Install Python Dependencies"
  │  └─ Comando: pip install -r backend/requirements.txt
  │
  └─ Step: "Build Backend"
     └─ Comando: python backend/setup.py build

Job 2: "Build Frontend"
  ├─ Step: "Install Node Dependencies"
  │  └─ Comando: cd frontend && npm install
  │
  └─ Step: "Build Frontend"
     └─ Comando: cd frontend && npm run build

Job 3: "Test All"
  ├─ Step: "Backend Tests"
  │  └─ Comando: pytest backend/tests/
  │
  ├─ Step: "Frontend Tests"
  │  └─ Comando: cd frontend && npm test
  │
  └─ Step: "Integration Tests"
     └─ Comando: npm run integration-test

Job 4: "Package"
  └─ Step: "Create Release"
     └─ Comando: bash scripts/create_release.sh

Job 5: "Deploy"
  ├─ Step: "Deploy to Staging"
  │  └─ Comando: kubectl apply -f k8s/staging/
  │
  └─ Step: "Deploy to Production"
     └─ Comando: kubectl apply -f k8s/production/
```

---

## 6. Pipeline Serverless (AWS Lambda)

**Caso de Uso**: Desplegar función Lambda

### Configuración

```
Nombre Pipeline: "Lambda Deploy"
Proyecto: "serverless-function"

Job 1: "Prepare"
  ├─ Step: "Install Dependencies"
  │  └─ Comando: pip install -r requirements.txt -t package/
  │
  └─ Step: "Copy Source"
     └─ Comando: cp lambda_function.py package/

Job 2: "Test"
  └─ Step: "Run Unit Tests"
     └─ Comando: pytest tests/ -v

Job 3: "Deploy"
  ├─ Step: "Create Zip"
  │  └─ Comando: cd package && zip -r ../lambda.zip .
  │
  ├─ Step: "Upload to S3"
  │  └─ Comando: aws s3 cp lambda.zip s3://lambda-bucket/
  │
  └─ Step: "Update Function"
     └─ Comando: aws lambda update-function-code --function-name my-function --s3-bucket lambda-bucket --s3-key lambda.zip
```

---

## 7. Pipeline Mobile (Flutter/React Native)

**Caso de Uso**: Compilar y probar aplicación móvil

### Configuración

```
Nombre Pipeline: "Mobile Build"
Proyecto: "flutter-app"

Job 1: "Setup"
  ├─ Step: "Get Dependencies"
  │  └─ Comando: flutter pub get
  │
  └─ Step: "Analyze Code"
     └─ Comando: flutter analyze

Job 2: "Test"
  ├─ Step: "Unit Tests"
  │  └─ Comando: flutter test
  │
  └─ Step: "Build APK"
     └─ Comando: flutter build apk --release

Job 3: "Build iOS"
  └─ Step: "Build IPA"
     └─ Comando: flutter build ios --release

Job 4: "Release"
  ├─ Step: "Upload to TestFlight"
  │  └─ Comando: fastlane ios upload_testflight
  │
  └─ Step: "Upload to Google Play"
     └─ Comando: fastlane android upload_play_store
```

---

## 8. Pipeline de Documentación

**Caso de Uso**: Compilar y publicar documentación

### Configuración

```
Nombre Pipeline: "Docs Deploy"
Proyecto: "documentation"

Job 1: "Build"
  ├─ Step: "Install Sphinx"
  │  └─ Comando: pip install sphinx sphinx-rtd-theme
  │
  └─ Step: "Build HTML"
     └─ Comando: make html -C docs/

Job 2: "Test"
  ├─ Step: "Check Links"
  │  └─ Comando: sphinx-linkcheck docs/
  │
  └─ Step: "Validate HTML"
     └─ Comando: html5validator --root docs/_build/html/

Job 3: "Deploy"
  └─ Step: "Upload to Hosting"
     └─ Comando: rsync -av docs/_build/html/ user@server:/var/www/docs/
```

---

## 9. Pipeline de Análisis de Código

**Caso de Uso**: Ejecutar análisis de seguridad y cobertura

### Configuración

```
Nombre Pipeline: "Security & Quality"
Proyecto: "secure-app"

Job 1: "Security"
  ├─ Step: "SAST Analysis"
  │  └─ Comando: sonarqube-scanner
  │
  ├─ Step: "Dependency Check"
  │  └─ Comando: dependency-check --scan .
  │
  └─ Step: "Secrets Scan"
     └─ Comando: truffleHog filesystem .

Job 2: "Quality"
  ├─ Step: "Code Coverage"
  │  └─ Comando: pytest --cov=app tests/
  │
  ├─ Step: "Complexity"
  │  └─ Comando: radon cc .
  │
  └─ Step: "Upload Report"
     └─ Comando: curl -X POST -F report=@coverage.xml server/api/reports
```

---

## 10. Pipeline Database Migration

**Caso de Uso**: Ejecutar migraciones de base de datos

### Configuración

```
Nombre Pipeline: "DB Migration"
Proyecto: "app-database"

Job 1: "Prepare"
  ├─ Step: "Install Tools"
  │  └─ Comando: npm install -g db-migrate
  │
  └─ Step: "Backup Database"
     └─ Comando: pg_dump dbname > backup.sql

Job 2: "Test Migration"
  ├─ Step: "Create Test DB"
  │  └─ Comando: createdb test_db
  │
  └─ Step: "Run Migration"
     └─ Comando: db-migrate up --test-env

Job 3: "Deploy"
  ├─ Step: "Run Migration Staging"
  │  └─ Comando: db-migrate up --env staging
  │
  └─ Step: "Run Migration Production"
     └─ Comando: db-migrate up --env production
```

---

## Tips para Crear Tus Propios Pipelines

1. **Define el objetivo**: ¿Qué quieres automatizar?
2. **Divide en jobs**: Agrupa tareas relacionadas
3. **Simplifica pasos**: Cada paso = un comando
4. **Ordena lógicamente**: compile → test → deploy
5. **Maneja errores**: Los pasos fallidos detienen el job
6. **Documenta**: Usa nombres descriptivos
7. **Reutiliza**: Guarda templates útiles

---

**¿Necesitas un pipeline personalizado?** Combina estos ejemplos según tus necesidades. 🚀
