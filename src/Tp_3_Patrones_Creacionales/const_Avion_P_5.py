# ---------------------------------------------------------
# PUNTO 5 - PATRÓN BUILDER (CONSTRUCCIÓN DE AVIONES)
# ---------------------------------------------------------
# Arquitectura: Separación de Construcción y Representación.
# Se utiliza para objetos complejos donde el orden de los pasos
# de creación es crítico. Cumple con la consigna de simplificar
# un avión en partes específicas.

from abc import ABC, abstractmethod

# ---------------------------------------------------------
# PRODUCTO: El objeto complejo a construir
# ---------------------------------------------------------
class Avion:
    """Clase que representa el producto final terminado."""
    def __init__(self):
        self.partes = []

    def mostrar_configuracion(self):
        # Muestra el listado de componentes instalados
        print("Configuración final del Avión: " + ", ".join(self.partes))


# ---------------------------------------------------------
# BUILDER ABSTRACTO: Define la interfaz de construcción
# ---------------------------------------------------------
class AvionBuilder(ABC):
    """Interfaz que define los pasos necesarios para crear un avión."""
    def __init__(self):
        self.avion = None

    def reset(self):
        self.avion = Avion()

    @abstractmethod
    def construir_body(self):
        pass

    @abstractmethod
    def construir_turbinas(self):
        pass

    @abstractmethod
    def construir_alas(self):
        pass

    @abstractmethod
    def construir_tren(self):
        pass

    def get_result(self):
        return self.avion


# ---------------------------------------------------------
# BUILDER CONCRETO: Implementación de la fabricación
# ---------------------------------------------------------
class AvionComercialBuilder(AvionBuilder):
    """Implementa los pasos de construcción específicos."""
    def construir_body(self):
        self.avion.partes.append("Body principal")

    def construir_turbinas(self):
        self.avion.partes.append("2 Turbinas")

    def construir_alas(self):
        self.avion.partes.append("2 Alas")

    def construir_tren(self):
        self.avion.partes.append("Tren de aterrizaje")


# ---------------------------------------------------------
# DIRECTOR: Controla el flujo de la construcción
# ---------------------------------------------------------
class Director:
    """Define el orden en el que se deben ejecutar los pasos."""
    def __init__(self, builder):
        self._builder = builder

    def fabricar_avion_completo(self):
        # Secuencia lógica de ensamblado
        self._builder.reset()
        self._builder.construir_body()
        self._builder.construir_turbinas()
        self._builder.construir_alas()
        self._builder.construir_tren()
        return self._builder.get_result()


# ---------------------------------------------------------
# EJECUCIÓN DEL PUNTO 5
# ---------------------------------------------------------

if __name__ == "__main__":
    # Se define el constructor específico
    constructor = AvionComercialBuilder()
    
    # El director coordina el proceso de fabricación
    oficina_tecnica = Director(constructor)
    
    # Se obtiene el producto final
    mi_avion = oficina_tecnica.fabricar_avion_completo()
    mi_avion.mostrar_configuracion()