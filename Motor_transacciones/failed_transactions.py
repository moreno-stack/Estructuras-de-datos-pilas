class FailedTransactions:

    def __init__(self, limit=5):
        self.limit = limit
        self.data = []

    def add(self, transaction):

        if len(self.data) >= self.limit:
            self.data.pop(0)

        self.data.append(transaction)

    def show(self):
        return self.data