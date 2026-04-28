# ---------------------------------------------------------
# PUNTO 7 - PATRÓN ABSTRACT FACTORY (FAMILIAS DE INTERFAZ)
# ---------------------------------------------------------
# Arquitectura: AbstractFactory.
# Se utiliza para crear familias de objetos relacionados (Botones, 
# Menúes, Ventanas) garantizando que los productos de una 
# familia sean compatibles entre sí sin especificar sus clases concretas.

from abc import ABC, abstractmethod

# -----------------------------------------------------------
# PRODUCTOS ABSTRACTOS: Definen las interfaces de la familia
# -----------------------------------------------------------
class Boton(ABC):
    """Interfaz para el componente Botón."""
    @abstractmethod
    def renderizar(self):
        pass

class Checkbox(ABC):
    """Interfaz para el componente Checkbox (extensión del ejemplo)."""
    @abstractmethod
    def renderizar(self):
        pass


# -----------------------------------------------------------
# PRODUCTOS CONCRETOS: Implementaciones por Sistema Operativo
# -----------------------------------------------------------
class BotonWindows(Boton):
    def renderizar(self):
        print("Renderizando: Botón con estilo visual de Windows.")

class CheckboxWindows(Checkbox):
    def renderizar(self):
        print("Renderizando: Checkbox con estilo visual de Windows.")

class BotonMac(Boton):
    def renderizar(self):
        print("Renderizando: Botón con estilo visual de MacOS.")

class CheckboxMac(Checkbox):
    def renderizar(self):
        print("Renderizando: Checkbox con estilo visual de MacOS.")


# ---------------------------------------------------------
# FÁBRICA ABSTRACTA: Define el contrato para la familia
# ---------------------------------------------------------
class UIFactory(ABC):
    """
    La Abstract Factory declara métodos para crear cada uno de 
    los productos abstractos de la familia.
    """
    @abstractmethod
    def crear_boton(self):
        pass

    @abstractmethod
    def crear_checkbox(self):
        pass


# --------------------------------------------------------------
# FÁBRICAS CONCRETAS: Instancian productos de una misma familia
# --------------------------------------------------------------
class WindowsFactory(UIFactory):
    def crear_boton(self):
        return BotonWindows()
    
    def crear_checkbox(self):
        return CheckboxWindows()

class MacFactory(UIFactory):
    def crear_boton(self):
        return BotonMac()
    
    def crear_checkbox(self):
        return CheckboxMac()


#  ---------------------------------------------------------
# EJECUCIÓN Y DEMOSTRACIÓN DEL PUNTO 7
# ----------------------------------------------------------

if __name__ == "__main__":
    # Supongamos que el sistema detecta que estamos en Windows
    # Se selecciona la fábrica correspondiente a la familia 'Windows'
    fabrica_actual = WindowsFactory()

    # El código cliente trabaja con las fábricas y productos 
    # únicamente a través de sus interfaces abstractas.
    boton = fabrica_actual.crear_boton()
    check = fabrica_actual.crear_checkbox()

    print("--- Generando Interfaz de Usuario ---")
    boton.renderizar()
    check.renderizar()