"""
Módulo para recuperación de tokens desde archivos JSON.
Refactorizado utilizando Programación Orientada a Objetos, patrón Singleton 
y la estrategia Branching by Abstraction.
"""

import json
import sys

class JSONTokenRetrieverSingleton:
    """
    Implementación del patrón Singleton para la recuperación de tokens.
    Garantiza que solo exista una instancia del recuperador en memoria.
    """
    _instance = None

    def __new__(cls):
        # Control de instancia única (Singleton)
        if cls._instance is None:
            cls._instance = super(JSONTokenRetrieverSingleton, cls).__new__(cls)
        return cls._instance

    def retrieve_token(self, filepath, key="token1"):
        """
        Abre el archivo JSON, extrae y retorna el valor de la clave especificada.
        Implementa programación defensiva para asegurar cierres controlados.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as json_file:
                data = json_file.read()

            obj = json.loads(data)

            if key in obj:
                return str(obj[key])
            
            print(f"Error: La clave '{key}' no se encuentra registrada en el archivo.")
            sys.exit(1)

        except FileNotFoundError:
            print(f"Error de E/S: No se pudo localizar el archivo en la ruta: '{filepath}'.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error de Integridad: El archivo provisto no posee una estructura JSON válida.")
            sys.exit(1)
        # pylint: disable=broad-exception-caught
        except Exception as error_inesperado:
            print(f"Error inesperado del sistema: {error_inesperado}")
            sys.exit(1)


# --- Branching by Abstraction ---
def token_retriever_abstraction(filepath, key="token1"):
    """
    Capa de abstracción que delega la funcionalidad de recuperación.
    En un proceso de re-ingeniería, esta interfaz permite a los clientes 
    (como la CLI) seguir funcionando mientras por debajo se cambia la 
    implementación legada por la nueva clase Singleton.
    """
    # Convergencia hacia la nueva implementación orientada a objetos
    retriever = JSONTokenRetrieverSingleton()
    return retriever.retrieve_token(filepath, key)


def main():
    """Función principal que maneja la interfaz de línea de comandos."""
    # g) Control de versión anticipado
    if "-v" in sys.argv:
        print("versión 1.1")
        sys.exit(0)

    # f) y c) Control robusto de argumentos mínimos de ejecución
    if len(sys.argv) < 2:
        print("Error: Argumentos insuficientes.")
        print("Uso correcto: python getJason.py <ruta_archivo_json> [clave_buscada]")
        print("Para ver la versión: python getJason.py -v")
        sys.exit(1)

    archivo_json = sys.argv[1]
    
    # Asignación dinámica de clave (Requerimiento de Reuso)
    clave_buscada = sys.argv[2] if len(sys.argv) >= 3 else "token1"

    # d) Ejecución a través de la capa de abstracción
    resultado = token_retriever_abstraction(archivo_json, clave_buscada)
    
    if resultado:
        print(resultado)

if __name__ == "__main__":
    main()