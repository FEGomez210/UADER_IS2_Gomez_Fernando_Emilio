# -------------------------------------------------------------------------
# Facultad: FCyT - UADER
# Alumno: Gómez, Fernando Emilio
# Cátedra: Ingeniería de Software II
# Profesor: Dr. Pedro E. Colla
# Ayudante: Lic. Lucía Blanc
# -------------------------------------------------------------------------

class TrenLaminador:
    """Interfaz para las implementaciones de los trenes de laminado."""
    def producir_plancha(self, e, a):
        pass

class Tren5Metros(TrenLaminador):
    """Implementación específica para producir planchas de 5 metros."""
    def producir_plancha(self, e, a):
        # Implementación concreta del tren de 5 metros
        return f"Plancha de {e}\" x {a}m x 5m de largo"

class Tren10Metros(TrenLaminador):
    """Implementación específica para producir planchas de 10 metros."""
    def producir_plancha(self, e, a):
        # Implementación concreta del tren de 10 metros
        return f"Plancha de {e}\" x {a}m x 10m de largo"

class LaminaAcero:
    """Abstracción que define el producto genérico."""
    def __init__(self, tren: TrenLaminador):
        # Desacopla la abstracción de su implementación física
        self.tren = tren
        self.espesor = 0.5 # Pulgadas constantes (consigna)
        self.ancho = 1.5   # Metros constantes (consigna)   

    def fabricar(self):
        """Delega la fabricación al tren laminador asignado."""
        # Mantiene alta cohesión al delegar la tarea específica
        resultado = self.tren.producir_plancha(self.espesor, self.ancho)
        print(f"Produciendo en planta: {resultado}")

# Ejemplo de uso
if __name__ == "__main__":
    plancha = LaminaAcero(Tren10Metros())
    plancha.fabricar()

