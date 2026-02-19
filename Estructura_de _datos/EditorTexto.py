class EditorTexto:

    def __init__(self):
        self.texto = ""
        self.pila_undo = []
        self.pila_redo = []

    def escribir(self, nuevo_texto):
        # Guardar estado actual en Undo
        self.pila_undo.append(self.texto)
        # Al escribir algo nuevo, se limpia Redo
        self.pila_redo.clear()
        self.texto += nuevo_texto
        print(f"Texto actual: '{self.texto}'")

    def borrar(self, cantidad):
        # Guardar estado actual en Undo
        self.pila_undo.append(self.texto)
        self.pila_redo.clear()
        self.texto = self.texto[:-cantidad]
        print(f"Texto actual: '{self.texto}'")

    def undo(self):
        if not self.pila_undo:
            print("No hay acciones para deshacer")
            return
        # Guardar estado actual en Redo
        self.pila_redo.append(self.texto)
        # Restaurar último estado
        self.texto = self.pila_undo.pop()
        print(f"Undo Texto actual: '{self.texto}'")

    def redo(self):
        if not self.pila_redo:
            print("No hay acciones para rehacer")
            return
        # Guardar estado actual en Undo
        self.pila_undo.append(self.texto)
        # Restaurar estado
        self.texto = self.pila_redo.pop()
        print(f"Redo  Texto actual: '{self.texto}'")

    def mostrar_pilas(self):
        print("ESTADO INTERNO")
        print("Texto:", self.texto)
        print("Pila Undo:", self.pila_undo)
        print("Pila Redo:", self.pila_redo)
        


# Simulación del caso de uso
editor = EditorTexto()

editor.escribir("Hola")
editor.escribir(" mundo")
editor.borrar(5)

editor.undo()
editor.undo()
editor.redo()

editor.mostrar_pilas()