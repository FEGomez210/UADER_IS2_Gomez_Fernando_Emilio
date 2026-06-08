import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def __init__(self):
        # Lista para almacenar hasta 4 mementos
        self.historial = []

    def save(self, writer):
        # Guardamos el estado actual
        self.historial.append(writer.save())
        # Si excedemos los 4 estados, eliminamos el más viejo (índice 0)
        if len(self.historial) > 4:
            self.historial.pop(0)

    def undo(self, writer, steps=0):
        """
        steps = 0: Recupera el estado inmediato anterior.
        steps = 1: Recupera el estado anterior a ese, etc (hasta 3).
        """
        # Calculamos el índice reverso. -1 es el último guardado.
        index = -1 - steps
        
        # Verificamos que el paso solicitado exista en el historial
        if abs(index) <= len(self.historial):
            estado_recuperado = self.historial[index]
            writer.undo(estado_recuperado)
            print(f"--- Undo ejecutado con nivel de retroceso: {steps} ---")
        else:
            print(f"Error: No hay suficientes estados guardados para retroceder {steps} pasos.")

if __name__ == '__main__':
    os.system("clear" if os.name == "posix" else "cls")
    
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    print("Grabando estado 1...")
    writer.write("Estado 1: Línea A\n")
    caretaker.save(writer)

    print("Grabando estado 2...")
    writer.write("Estado 2: Línea B\n")
    caretaker.save(writer)

    print("Grabando estado 3...")
    writer.write("Estado 3: Línea C\n")
    caretaker.save(writer)

    print("Grabando estado 4...")
    writer.write("Estado 4: Línea D\n")
    caretaker.save(writer)
    
    print("\nContenido actual (Estado 4):")
    print(writer.content)

    print("Recuperando el inmediato anterior (steps = 0)")
    # El inmediato anterior al actual en realidad es el mismo estado 4 si acabamos de guardar, 
    # pero para retroceder un paso útil aplicamos steps=1 para ver el Estado 3, etc.
    # Siguiendo la consigna, 0 es el inmediato anterior.
    caretaker.undo(writer, 0) 
    print(writer.content)

    print("Recuperando 2 pasos atrás (steps = 2)")
    caretaker.undo(writer, 2)
    print(writer.content)

    print("Recuperando el más antiguo disponible (steps = 3)")
    caretaker.undo(writer, 3)
    print(writer.content)
    