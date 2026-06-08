import os

# Iterador Directo (Izquierda a Derecha)
class IteradorDirecto:
    def __init__(self, cadena):
        self.cadena = cadena
        self.indice = 0

    def tiene_siguiente(self):
        return self.indice < len(self.cadena)

    def siguiente(self):
        if self.tiene_siguiente():
            caracter = self.cadena[self.indice]
            self.indice += 1
            return caracter
        return None

# Iterador Reverso (Derecha a Izquierda)
class IteradorReverso:
    def __init__(self, cadena):
        self.cadena = cadena
        self.indice = len(self.cadena) - 1

    def tiene_siguiente(self):
        return self.indice >= 0

    def siguiente(self):
        if self.tiene_siguiente():
            caracter = self.cadena[self.indice]
            self.indice -= 1
            return caracter
        return None

# Colección Iterable
class ColeccionCadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def get_iterador_directo(self):
        return IteradorDirecto(self.cadena)

    def get_iterador_reverso(self):
        return IteradorReverso(self.cadena)

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    
    texto = "UADER FCyT"
    coleccion = ColeccionCadena(texto)

    print(f"Cadena original: '{texto}'\n")

    print("Recorrido Directo:")
    iterador_dir = coleccion.get_iterador_directo()
    while iterador_dir.tiene_siguiente():
        print(iterador_dir.siguiente(), end="-")
    print("\n")

    print("Recorrido Reverso:")
    iterador_rev = coleccion.get_iterador_reverso()
    while iterador_rev.tiene_siguiente():
        print(iterador_rev.siguiente(), end="-")
    print("\n")
    