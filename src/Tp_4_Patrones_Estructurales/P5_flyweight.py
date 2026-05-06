# -------------------------------------------------------------------------
# Facultad: FCyT - UADER
# Alumno: Gómez, Fernando Emilio
# Cátedra: Ingeniería de Software II
# Profesor: Dr. Pedro E. Colla
# Ayudante: Lic. Lucía Blanc
# -------------------------------------------------------------------------

class ModeloArbol:
    """
    Estado Intrínseco (Flyweight): Contiene los datos compartidos.
    En un entorno real, aquí irían texturas de alta resolución o 
    mallas poligonales pesadas.
    """
    def __init__(self, nombre, color, textura):
        self.nombre = nombre
        self.color = color
        self.textura = textura  # Imagina que esto pesa varios MB

    def dibujar(self, x, y):
        # Muestra cómo se combinan los datos compartidos con los únicos
        print(f"Dibujando '{self.nombre}' ({self.color}) en pos: [{x}, {y}]")


class FabricaDeArboles:
    """
    El Flyweight Factory: Asegura que los objetos compartidos se reutilicen.
    Mantiene un pool de modelos para no duplicar memoria.
    """
    _modelos = {}

    @classmethod
    def obtener_modelo(cls, nombre, color, textura):
        llave = (nombre, color, textura)
        if llave not in cls._modelos:
            print(f"--- Creando nuevo modelo de árbol: {nombre} ---")
            cls._modelos[llave] = ModeloArbol(nombre, color, textura)
        return cls._modelos[llave]


class ArbolIndividual:
    """
    Estado Extrínseco: Contiene los datos únicos de cada instancia.
    Solo guarda las coordenadas y una referencia al modelo compartido.
    """
    def __init__(self, x, y, modelo: ModeloArbol):
        self.x = x
        self.y = y
        self.modelo = modelo

    def mostrar(self):
        # Delega el renderizado al modelo compartido pasando su estado único
        self.modelo.dibujar(self.x, self.y)


# --- TEST LOCAL PARA EL PUNTO 5 ---
if __name__ == "__main__":
    print("\n=== TEST 5: PATRÓN FLYWEIGHT ===")
    fabrica = FabricaDeArboles()

    # Definimos 10,000 árboles, pero solo 2 modelos reales en memoria
    bosque = []
    
    # Creamos muchos Robles (comparten el mismo modelo)
    modelo_roble = fabrica.obtener_modelo("Roble", "Verde Oscuro", "textura_roble_4k.png")
    for i in range(5):
        bosque.append(ArbolIndividual(i*10, i*15, modelo_roble))

    # Creamos muchos Pinos (comparten el mismo modelo)
    modelo_pino = fabrica.obtener_modelo("Pino", "Verde Claro", "textura_pino_4k.png")
    for i in range(5):
        bosque.append(ArbolIndividual(i*12, i*22, modelo_pino))

    print("\nRenderizando Bosque Eficiente:")
    for arbol in bosque:
        arbol.mostrar()

    print(f"\nResumen de memoria: {len(bosque)} árboles creados, pero solo {len(FabricaDeArboles._modelos)} modelos en RAM.")