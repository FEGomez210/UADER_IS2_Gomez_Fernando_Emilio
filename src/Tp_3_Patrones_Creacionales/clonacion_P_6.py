# ---------------------------------------------------------
# PUNTO 6 - PATRÓN PROTOTYPE (CLONACIÓN DE OBJETOS)
# ---------------------------------------------------------
# Arquitectura: Prototype.
# Este patrón permite crear nuevas instancias a partir de una 
# existente. La consigna requiere verificar que un objeto 
# clonado pueda generar sus propias copias (clonación en cadena).

import copy
from abc import ABC, abstractmethod

class IPrototipo(ABC):
    @abstractmethod
    def clonar(self):
        """Método para obtener una copia de la instancia."""
        pass

# ---------------------------------------------------------
# CLASE CONCRETA: Implementa la capacidad de duplicarse
# ---------------------------------------------------------
class Componente(IPrototipo):
    """
    Clase que permite obtener copias de sí misma sin 
    depender de la creación directa vía constructor.
    """
    def __init__(self, valor):
        self.valor = valor

    def clonar(self):
        # copy.deepcopy realiza una copia profunda de todos 
        # los atributos, asegurando independencia total en memoria.
        return copy.deepcopy(self)


# ---------------------------------------------------------
# EJECUCIÓN Y VERIFICACIÓN DEL PUNTO 6
# ---------------------------------------------------------

if __name__ == "__main__":
    # 1. Creación del objeto prototipo original
    original = Componente(100)
    print("Objeto Original - Valor: " + str(original.valor))

    # 2. Primera clonación (P1 -> P2)
    clon_uno = original.clonar()
    print("Primer Clon - Valor: " + str(clon_uno.valor))

    # 3. Verificación de clonación encadenada (P2 -> P3)
    # Se demuestra que el clon también puede obtener copias de sí mismo.
    clon_dos = clon_uno.clonar()
    print("Segundo Clon (desde el primero) - Valor: " + str(clon_dos.valor))

    # 4. Prueba de independencia (Arquitectura de Software)
    # Verificamos que las direcciones de memoria sean distintas.
    print("\n--- Verificación de Independencia en Memoria ---")
    print("¿Original y Clon 1 son el mismo objeto?: " + str(original is clon_uno))
    print("¿Clon 1 y Clon 2 son el mismo objeto?: " + str(clon_uno is clon_dos))