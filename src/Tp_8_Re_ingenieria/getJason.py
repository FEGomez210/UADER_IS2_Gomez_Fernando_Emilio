"""
copyright UADERFCyT-IS2©2024 todos los derechos reservados

Módulo para procesamiento de pagos automatizado.
Versión 1.2 - Re-Ingeniería aplicando Patrones Singleton, 
Chain of Responsibility (Cadena de Mando) e Iterator.
"""

import json
import sys

class JSONTokenRetrieverSingleton:
    """
    Patrón Singleton: Garantiza una única instancia en memoria para
    la recuperación de claves bancarias desde un archivo de configuración.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JSONTokenRetrieverSingleton, cls).__new__(cls)
        return cls._instance

    def retrieve_token(self, filepath, key):
        """Lee el archivo JSON y devuelve el valor real del token."""
        try:
            with open(filepath, 'r', encoding='utf-8') as json_file:
                data = json_file.read()
            obj = json.loads(data)
            
            if key in obj:
                return str(obj[key])
            return f"Token_Desconocido({key})"
            
        except FileNotFoundError:
            return "Error: Archivo no encontrado"
        except json.JSONDecodeError:
            return "Error: JSON Invalido"


# --- Patrón Iterator ---
class IteradorPagos:
    """Implementación del iterador para recorrer el historial cronológico."""
    def __init__(self, lista_pagos):
        self._lista_pagos = lista_pagos
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < len(self._lista_pagos):
            pago = self._lista_pagos[self._indice]
            self._indice += 1
            return pago
        raise StopIteration


class HistorialPagos:
    """Colección que almacena los registros de pagos y provee su iterador."""
    def __init__(self):
        self.pagos = []

    def registrar_pago(self, id_pedido, token_id, token_real, monto):
        """Añade un pago estructurado a la memoria del historial."""
        self.pagos.append({
            "pedido": id_pedido,
            "token_id": token_id,
            "token_real": token_real,
            "monto": monto
        })

    def __iter__(self):
        return IteradorPagos(self.pagos)


# --- Patrón Chain of Responsibility (Cadena de Mando) ---
class ManejadorPago:
    """
    Eslabón de la cadena. Representa una cuenta bancaria. 
    Procesa el pago si tiene saldo, sino, lo deriva al siguiente sucesor.
    """
    def __init__(self, token_id, saldo_inicial):
        self.token_id = token_id
        self.saldo = saldo_inicial
        self.sucesor = None

    def set_sucesor(self, sucesor):
        """Define dinámicamente quién es el próximo eslabón a consultar."""
        self.sucesor = sucesor

    def procesar(self, id_pedido, monto, historial):
        """Intenta debitar el saldo o delega la responsabilidad."""
        if self.saldo >= monto:
            self.saldo -= monto
            
            # Integración del Singleton del punto anterior
            retriever = JSONTokenRetrieverSingleton()
            token_real = retriever.retrieve_token('sitedata.json', self.token_id)
            
            historial.registrar_pago(id_pedido, self.token_id, token_real, monto)
            return True
        
        # Si no hay saldo, y hay un sucesor configurado, se le pasa la orden
        if self.sucesor:
            return self.sucesor.procesar(id_pedido, monto, historial)
        
        # Si nadie en la cadena tiene fondos
        return False


class ProcesadorPagos:
    """
    Cliente orquestador. Configura la Cadena de Mando en cada ciclo 
    para garantizar el balanceo (ruteo alternativo) de las cuentas.
    """
    def __init__(self):
        # Inicialización según requerimiento d)
        self.cuenta1 = ManejadorPago("token1", 1000)
        self.cuenta2 = ManejadorPago("token2", 2000)
        self.turno = 1
        self.historial = HistorialPagos()

    def ejecutar_pago(self, id_pedido, monto):
        """
        Rutea alternativamente. Configura la cadena T1->T2 o T2->T1
        dependiendo de a quién le toca el turno primario.
        """
        if self.turno == 1:
            self.cuenta1.set_sucesor(self.cuenta2)
            self.cuenta2.set_sucesor(None)
            resultado = self.cuenta1.procesar(id_pedido, monto, self.historial)
            self.turno = 2
        else:
            self.cuenta2.set_sucesor(self.cuenta1)
            self.cuenta1.set_sucesor(None)
            resultado = self.cuenta2.procesar(id_pedido, monto, self.historial)
            self.turno = 1
            
        return resultado

    def listar_pagos_cronologicos(self):
        """Consume el patrón Iterator para imprimir los resultados."""
        print("\n--- Historial Cronológico de Pagos Procesados ---")
        # El bucle 'for' consume internamente el __iter__ y __next__
        for pago in self.historial:
            print(f"Pedido N° {pago['pedido']:02d} | "
                  f"Cuenta: {pago['token_id']} | "
                  f"Token Físico: {pago['token_real']} | "
                  f"Monto: ${pago['monto']}")
        print("-------------------------------------------------")


def main():
    """Punto de entrada principal y simulación de pagos."""
    # f) Avance de versión a 1.2
    if len(sys.argv) > 1 and sys.argv[1] == "-v":
        print("versión 1.2")
        sys.exit(0)

    print("Iniciando motor de pagos re-ingenierizado (Versión 1.2)...")
    procesador = ProcesadorPagos()
    
    # e) Simulación de pedidos de pago de $500.-
    monto_pedido = 500
    
    # Simulamos 7 pedidos para forzar a que las cuentas se queden sin saldo
    # y demostrar el funcionamiento del fallback en la Cadena de Mando.
    for i in range(1, 8):
        print(f"-> Ingresando pedido N° {i} por ${monto_pedido}...")
        exito = procesador.ejecutar_pago(i, monto_pedido)
        if not exito:
            print(f"   [!] Pedido N° {i} RECHAZADO: Todas las cuentas sin fondos.")

    # Listado final
    procesador.listar_pagos_cronologicos()


if __name__ == "__main__":
    main()