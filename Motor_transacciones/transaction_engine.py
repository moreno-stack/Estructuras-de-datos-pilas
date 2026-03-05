import random
from stack_manager import TransactionStack

class TransactionEngine:

    def process(self, transaction):

        stack = TransactionStack()

        pasos = [
            "Confirmar transaccion",
            "Acreditar destino",
            "Descontar saldo",
            "Validar saldo",
            "Validar cuentas"
        ]

        for p in pasos:
            stack.push(p)

        while not stack.is_empty():

            paso = stack.pop()

            if random.randint(1,10) == 1:
                return False

        return True