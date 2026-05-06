# -------------------------------------------------------------------------
# Facultad: FCyT - UADER
# Alumno: Gómez, Fernando Emilio
# Cátedra: Ingeniería de Software II
# Profesor: Dr. Pedro E. Colla
# Ayudante: Lic. Lucía Blanc
# -------------------------------------------------------------------------

class ComponenteEnsamblado:
    """Clase base para piezas simples y sub-conjuntos compuestos."""
    def mostrar(self, nivel=0):
        pass

class PiezaIndividual(ComponenteEnsamblado):
    """Nodo hoja: representa una pieza que no contiene otras."""
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        # Representación visual jerárquica mediante indentación
        print("  " * nivel + f"|_ Pieza: {self.nombre}")

class SubConjunto(ComponenteEnsamblado):
    """Nodo compuesto: contiene una lista de otros componentes."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, componente: ComponenteEnsamblado):
        """Añade una pieza o sub-conjunto a la lista de hijos."""
        # Permite la construcción de árboles de ensamblado
        self.elementos.append(componente)

    def mostrar(self, nivel=0):
        """Muestra el nombre del conjunto y recorre sus hijos."""
        print("  " * nivel + f"+ Conjunto: {self.nombre}")
        for item in self.elementos:
            # Polimorfismo para tratar hojas y ramas por igual
            item.mostrar(nivel + 1)

# Construcción de la estructura según el TP4
if __name__ == "__main__":
    ensamblado_maestro = SubConjunto("Producto Principal")
    for i in range(1, 4):
        sc = SubConjunto(f"SC-{i}")
        for j in range(1, 5):
            sc.agregar(PiezaIndividual(f"P{j}-SC{i}"))
        ensamblado_maestro.agregar(sc)
    ensamblado_maestro.mostrar()

