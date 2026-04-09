# Caso de Estudio: Gestión de Turnos con Lista Doble en Python

Este proyecto muestra un caso de estudio real usando una lista doblemente enlazada (`DoublyLinkedList`) en Python, con una pequeña interfaz web para manipular los datos.

## Descripción

- Caso: gestión de turnos en una clínica o consultorio.
- Estructura: se usa una lista doble para representar la cola de atención.
- Beneficio: navegar hacia adelante y hacia atrás, mover turnos y conservar referencias previas y siguientes.

## Archivos principales

- `lista_doble.py`: implementación de la lista doblemente enlazada, con operaciones de inserción por prioridad, eliminación, búsqueda, actualización y movimiento.
- `routes.py`: rutas Flask, manejo de turnos y lógica de navegación.
- `app.py`: arranque de la aplicación y registro del blueprint.
- `templates/base.html`: plantilla base compartida para la interfaz.
- `templates/index.html`: página principal extendiendo la plantilla base.
- `static/styles.css`: estilos modernos para la página web.

## Nuevas funciones

- Ficha de salida: registra turnos atendidos y elimina el turno de la cola.
- Resumen de jornada: muestra turnos pendientes, atendidos, próximo turno y última salida.
- Historial de salidas: lista de turnos que ya fueron atendidos durante la sesión.

## Requisitos

- Python 3.8+
- Flask

## Instalación

1. Crear un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar Flask:

```powershell
pip install Flask
```

## Uso

```powershell
python app.py
```

Luego abre `http://127.0.0.1:5000/` en el navegador.

## Qué demuestra este caso de estudio

- Inserción ordenada por prioridad en una lista doble.
- Eliminación segura de cualquier nodo.
- Movimientos hacia arriba y hacia abajo sin reconstruir la lista completa.
- Interfaz web para visualizar cómo cambia la estructura en tiempo real.

## Nota

El ejemplo está diseñado para ser fácil de ejecutar pero suficientemente completo para apreciar las diferencias entre una lista simple y una lista doblemente enlazada.
