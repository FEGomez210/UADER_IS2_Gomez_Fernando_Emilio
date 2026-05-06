# -------------------------------------------------------------------------
# Facultad: FCyT - UADER
# Alumno: Gómez, Fernando Emilio
# Cátedra: Ingeniería de Software II
# Profesor: Dr. Pedro E. Colla
# Ayudante: Lic. Lucía Blanc
# -------------------------------------------------------------------------

class ModeloMadera:
    """
    Estado Intrínseco: Información pesada compartida entre miles de unidades.
    """
    def __init__(self, tipo, resistencia, imagen_tecnica):
        self.tipo = tipo
        self.resistencia = resistencia
        self.imagen_tecnica = imagen_tecnica # Datos pesados (MBs)

    def mostrar_detalle(self, id_serie):
        print(f"ID: {id_serie} | Madera: {self.tipo} | Resistencia: {self.resistencia}")


class FabricaDeModelos:
    """Gestor de Flyweights para evitar duplicados en RAM."""
    _modelos = {}

    @classmethod
    def obtener_modelo(cls, tipo, resistencia, imagen):
        if tipo not in cls._modelos:
            cls._modelos[tipo] = ModeloMadera(tipo, resistencia, imagen)
        return cls._modelos[tipo]


class UnidadStock:
    """
    Estado Extrínseco: Datos únicos por cada pieza física en el depósito.
    """
    def __init__(self, id_serie, modelo: ModeloMadera):
        self.id_serie = id_serie
        self.modelo = modelo

    def listar(self):
        # Combina el ID único con los datos pesados compartidos
        self.modelo.mostrar_detalle(self.id_serie)

# --- Test de la Maderera ---
if __name__ == "__main__":
    print("=== GESTIÓN DE STOCK MADERERA (FLYWEIGHT) ===")
    fabrica = FabricaDeModelos()
    
    # Se cargan 2 modelos pesados una sola vez
    m_pino = fabrica.obtener_modelo("Pino", "Media", "foto_pino_HD.raw")
    m_euca = fabrica.obtener_modelo("Eucalipto", "Alta", "foto_euca_HD.raw")

    # Se crean 10.000 unidades en stock usando solo esos 2 modelos
    deposito = [UnidadStock(f"SERIE-{i}", m_pino if i % 2 == 0 else m_euca) for i in range(10000)]

    # Mostramos los primeros 5 para verificar
    for unidad in deposito[:5]:
        unidad.listar()

    print(f"\nÉxito: {len(deposito)} unidades procesadas usando solo {len(FabricaDeModelos._modelos)} objetos pesados.")

    