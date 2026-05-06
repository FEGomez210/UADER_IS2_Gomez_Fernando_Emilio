# -------------------------------------------------------------------------
# Facultad: FCyT - UADER
# Alumno: Gómez, Fernando Emilio
# Cátedra: Ingeniería de Software II
# Profesor: Dr. Pedro E. Colla
# Ayudante: Lic. Lucía Blanc
# -------------------------------------------------------------------------

class ComponenteNumero:
    """Interfaz que define la operación base de obtener valor."""
    def calcular(self):
        pass

class NumeroBase(ComponenteNumero):
    """Componente concreto que almacena el valor inicial."""
    def __init__(self, valor):
        self.valor = valor

    def calcular(self):
        # Retorna el valor base sin transformaciones
        return self.valor

class DecoradorMatematico(ComponenteNumero):
    """Base para los decoradores que mantienen la referencia al objeto."""
    def __init__(self, componente: ComponenteNumero):
        self._componente = componente

class SumarDos(DecoradorMatematico):
    """Añade 2 al resultado del componente envuelto."""
    def calcular(self):
        # Agrega responsabilidad dinámica al cálculo anterior
        return self._componente.calcular() + 2

class MultiplicarPorDos(DecoradorMatematico):
    """Multiplica por 2 el resultado del componente envuelto."""
    def calcular(self):
        return self._componente.calcular() * 2

class DividirPorTres(DecoradorMatematico):
    """Divide por 3 el resultado del componente envuelto."""
    def calcular(self):
        return self._componente.calcular() / 3

# Ejemplo de invocación anidada según requerimiento
if __name__ == "__main__":
    base = NumeroBase(10)
    # Estructura decorada: ((10 + 2) * 2) / 3 
    decorado = DividirPorTres(MultiplicarPorDos(SumarDos(base)))
    print(f"Resultado final con decoración: {decorado.calcular()}")

