# Motor de Transacciones Bancarias

Este proyecto simula un sistema de procesamiento de transacciones bancarias
utilizando estructuras de datos fundamentales.

Estructuras utilizadas:

Colas (Queue)
Se usan para almacenar transacciones entrantes que aún no han sido procesadas.

Pilas (Stack)
Se usan para ejecutar los pasos de cada transferencia:
- Validar cuenta
- Descontar dinero
- Acreditar destino
- Confirmar transacción

Arreglos
Se usan para almacenar las últimas transacciones fallidas para auditoría.

Frontend
Se implementa una interfaz por consola para que el usuario pueda:

1. Crear transacciones
2. Procesarlas
3. Ver cola de transacciones
4. Ver historial de fallos

Ejecución del proyecto:

python main.py