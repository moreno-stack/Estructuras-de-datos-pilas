from queue_manager import TransactionQueue
from transaction_engine import TransactionEngine
from failed_transactions import FailedTransactions

class Frontend:

    def __init__(self):

        self.queue = TransactionQueue()
        self.engine = TransactionEngine()
        self.failed = FailedTransactions()

    def menu(self):

        while True:

            print("\n--- MOTOR DE TRANSACCIONES ---")
            print("1. Nueva transaccion")
            print("2. Procesar transaccion")
            print("3. Ver cola")
            print("4. Ver fallidas")
            print("5. Salir")

            op = input("Seleccione: ")

            if op == "1":

                origen = input("Cuenta origen: ")
                destino = input("Cuenta destino: ")
                monto = input("Monto: ")

                transaction = {
                    "origen": origen,
                    "destino": destino,
                    "monto": monto
                }

                self.queue.add_transaction(transaction)

            elif op == "2":

                t = self.queue.get_transaction()

                if t is None:
                    print("No hay transacciones.")
                else:

                    ok = self.engine.process_transaction(t)

                    if not ok:
                        self.failed.add_failed(t)

            elif op == "3":
                print(self.queue.show_queue())

            elif op == "4":
                print(self.failed.get_failed())

            elif op == "5":
                break