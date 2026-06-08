import os

# Interfaz base para los manejadores
class Manejador:
    def __init__(self, sucesor=None):
        self.sucesor = sucesor

    def manejar(self, numero):
        if self.sucesor:
            self.sucesor.manejar(numero)

# Eslabón 1: Consumidor de Primos
class ManejadorPrimos(Manejador):
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def manejar(self, numero):
        if self.es_primo(numero):
            print(f"Primo: El número {numero} fue consumido.")
        else:
            # Si no es primo, lo pasa al siguiente en la cadena
            super().manejar(numero)

# Eslabón 2: Consumidor de Pares
class ManejadorPares(Manejador):
    def manejar(self, numero):
        # Si es par (y no fue consumido por primos antes)
        if numero % 2 == 0:
            print(f"Par: El número {numero} fue consumido.")
        else:
            super().manejar(numero)

# Eslabón 3: No consumidos
class ManejadorNoConsumido(Manejador):
    def manejar(self, numero):
        print(f"No Consumido: El número {numero} llegó al final de la cadena.")

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    
    # Armamos la cadena: Primos -> Pares -> No consumidos
    cadena = ManejadorPrimos(ManejadorPares(ManejadorNoConsumido()))
    
    print("Iniciando cadena de responsabilidad (1 al 100)...\n")
    for i in range(1, 101):
        cadena.manejar(i)

