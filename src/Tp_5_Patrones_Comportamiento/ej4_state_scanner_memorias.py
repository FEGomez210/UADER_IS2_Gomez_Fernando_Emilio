import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a Memorias")
        self.radio.state = self.radio.memory_state

# NUEVO: Implementa como barrer las estaciones guardadas en Memoria
class MemoryState(State):
    def __init__(self, radio):
        self.radio = radio
        # M1 a M4 combinando AM y FM
        self.stations = ["M1 (1380 AM)", "M2 (89.1 FM)", "M3 (103.9 FM)", "M4 (1510 AM)"]
        self.pos = 0
        self.name = "MEMORIA"

    def scan(self):
        # Barre siempre las 4 memorias en cada ciclo
        print("\n--- Iniciando barrido de Memorias ---")
        for memoria in self.stations:
            print(f"Sintonizando Memoria... {memoria}")
        print("--- Fin de barrido de Memorias ---\n")

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.memory_state = MemoryState(self) # Agregamos estado de memoria
        self.state = self.fmstate # Inicial en FM

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    print("Radio con barrido de Memorias M1 a M4")
    radio = Radio()
    
    # Secuencia de prueba: Escanea en FM, pasa a Memoria, escanea Memoria, pasa a AM
    radio.scan()
    radio.toggle_amfm() # Pasa a memoria
    radio.scan()        # Ejecuta el barrido de M1 a M4
    radio.toggle_amfm() # Pasa a AM
    radio.scan()

