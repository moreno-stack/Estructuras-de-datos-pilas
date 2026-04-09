class Node:
    def __init__(self, nombre: str, prioridad: int):
        self.nombre = nombre
        self.prioridad = prioridad
        self.prev = None
        self.next = None

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "prioridad": self.prioridad,
        }


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.head is None

    def add_end(self, nombre: str, prioridad: int):
        node = Node(nombre, prioridad)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return node

    def add_start(self, nombre: str, prioridad: int):
        node = Node(nombre, prioridad)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        return node

    def add_priority(self, nombre: str, prioridad: int):
        if self.is_empty():
            return self.add_end(nombre, prioridad)

        current = self.head
        while current and current.prioridad <= prioridad:
            current = current.next

        if current is None:
            return self.add_end(nombre, prioridad)

        if current is self.head:
            return self.add_start(nombre, prioridad)

        node = Node(nombre, prioridad)
        previous = current.prev
        previous.next = node
        node.prev = previous
        node.next = current
        current.prev = node
        return node

    def find(self, nombre: str):
        current = self.head
        while current:
            if current.nombre == nombre:
                return current
            current = current.next
        return None

    def remove(self, nombre: str) -> bool:
        node = self.find(nombre)
        if not node:
            return False

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = node.next = None
        return True

    def update_prio(self, nombre: str, prioridad: int) -> bool:
        node = self.find(nombre)
        if not node:
            return False
        self.remove(nombre)
        self.add_priority(nombre, prioridad)
        return True

    def move(self, nombre: str, direction: str) -> bool:
        node = self.find(nombre)
        if not node:
            return False

        if direction == "up" and node.prev:
            previous = node.prev
            prev_prev = previous.prev
            next_node = node.next

            if prev_prev:
                prev_prev.next = node
            node.prev = prev_prev
            node.next = previous
            previous.prev = node
            previous.next = next_node
            if next_node:
                next_node.prev = previous

            if previous is self.head:
                self.head = node

            if node is self.tail:
                self.tail = previous

            if self.tail and self.tail.next:
                self.tail = self.tail.next
            return True

        if direction == "down" and node.next:
            next_node = node.next
            next_next = next_node.next
            prev_node = node.prev

            if prev_node:
                prev_node.next = next_node
            next_node.prev = prev_node
            next_node.next = node
            node.prev = next_node
            node.next = next_next
            if next_next:
                next_next.prev = node

            if node is self.head:
                self.head = next_node

            if next_node is self.tail:
                self.tail = node
            return True

        return False

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.to_dict())
            current = current.next
        return result


def demo():
    lista = DoublyLinkedList()
    lista.add_priority("Recepción de pacientes", 3)
    lista.add_priority("Urgencias", 1)
    lista.add_priority("Consulta general", 4)
    lista.add_priority("Entrega de recetas", 5)
    lista.add_priority("Pruebas de laboratorio", 2)

    print("Lista de turnos ordenada por prioridad:")
    for item in lista.to_list():
        print(item)

    lista.move("Consulta general", "up")
    lista.update_prio("Entrega de recetas", 1)
    lista.remove("Recepción de pacientes")

    print("\nDespués de mover, actualizar y eliminar:")
    for item in lista.to_list():
        print(item)


if __name__ == "__main__":
    demo()
