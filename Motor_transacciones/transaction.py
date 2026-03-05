class Transaction:

    def __init__(self, id, origen, destino, monto):
        self.id = id
        self.origen = origen
        self.destino = destino
        self.monto = monto

    def __str__(self):
        return f"{self.id} | {self.origen} -> {self.destino} | ${self.monto}"