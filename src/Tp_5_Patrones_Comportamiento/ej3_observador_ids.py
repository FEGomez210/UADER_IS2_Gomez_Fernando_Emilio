import os

# El Sujeto (SujetoEmisor)
class Emisor:
    def __init__(self):
        self.observadores = []

    def suscribir(self, observador):
        self.observadores.append(observador)

    def emitir_id(self, id_emitido):
        print(f"\n--- Emisor genera el ID: {id_emitido} ---")
        # Notificamos a todos los suscriptores
        for obs in self.observadores:
            obs.actualizar(id_emitido)

# El Observador
class Suscriptor:
    def __init__(self, nombre, id_esperado):
        self.nombre = nombre
        self.id_esperado = id_esperado

    def actualizar(self, id_recibido):
        # Solo reacciona si el ID coincide
        if self.id_esperado == id_recibido:
            print(f"[{self.nombre}] ¡Match! He recibido mi ID esperado: {id_recibido}")

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    
    emisor = Emisor()

    # Instanciamos 4 clases (suscriptores) con IDs de 4 caracteres
    obs1 = Suscriptor("Clase 1", "A111")
    obs2 = Suscriptor("Clase 2", "B222")
    obs3 = Suscriptor("Clase 3", "C333")
    obs4 = Suscriptor("Clase 4", "D444")

    # Los suscribimos
    emisor.suscribir(obs1)
    emisor.suscribir(obs2)
    emisor.suscribir(obs3)
    emisor.suscribir(obs4)

    # Lista de 8 IDs a emitir (4 coinciden, 4 son basura)
    ids_a_emitir = ["X999", "A111", "Z000", "B222", "C333", "H555", "D444", "Y888"]

    for codigo in ids_a_emitir:
        emisor.emitir_id(codigo)
        