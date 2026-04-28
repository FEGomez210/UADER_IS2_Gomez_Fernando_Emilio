# -----------------------------------------
# PUNTO 1 - SINGLETON (FACTORIAL)
# -----------------------------------------

# Singleton: asegura una única instancia de la clase

class Factorial:
    _instance = None  # instancia única

    def __new__(cls):
        # Control de creación de instancia
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular(self, n):
        # Método recursivo para factorial
        if n <= 1:
            return 1
        return n * self.calcular(n - 1)


def main():
    f1 = Factorial()
    f2 = Factorial()

    print("¿Misma instancia?", f1 is f2)
    print("Factorial de 5:", f1.calcular(5))


if __name__ == "__main__":
    main()