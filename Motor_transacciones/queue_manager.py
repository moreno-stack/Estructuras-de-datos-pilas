from collections import deque

class TransactionQueue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, transaction):
        self.queue.append(transaction)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def show(self):
        return list(self.queue)