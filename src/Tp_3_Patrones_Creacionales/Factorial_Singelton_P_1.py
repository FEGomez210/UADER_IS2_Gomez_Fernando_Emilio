# ---------------------------------------------------------
# PUNTO 1 - PATRÓN SINGLETON (CÁLCULO DE FACTORIAL)
# ----------------------------------------------------------
# Arquitectura: Instancia Única de Servicio Matemático.
# Según la consigna, se debe asegurar que todas las clases 
# que invoquen el cálculo del factorial utilicen la misma 
# instancia de clase.

class Factorial:
    # Atributo de clase privado para la instancia única
    _instance = None 

    def __new__(cls):
        # Intercepta la creación del objeto para aplicar Singleton.
        # Si la instancia no existe, se crea mediante super().
        if cls._instance is None:
            cls._instance = super(Factorial, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        """
        Calcula el factorial de un número entero.
        Implementación mediante recursión lógica.
        """
        if n <= 1:
            return 1
        return n * self.calcular(n - 1)


# ---------------------------------------------------------
# VERIFICACIÓN DE ARQUITECTURA (PUNTO 1)
# ---------------------------------------------------------

if __name__ == "__main__":
    # 1. Intento de crear dos instancias por separado
    instancia_a = Factorial()
    instancia_b = Factorial()

    # 2. Comprobación de identidad (Métrica de Singleton)
    # Debe retornar True, confirmando que ocupan el mismo espacio en memoria.
    print("--- Verificación Punto 1: Singleton ---")
    print("¿Utilizan la misma instancia?: " + str(instancia_a is instancia_b))

    # 3. Ejecución del cálculo solicitado
    numero = 5
    resultado = instancia_a.calcular(numero)
    print("Resultado del Factorial de " + str(numero) + ": " + str(resultado))