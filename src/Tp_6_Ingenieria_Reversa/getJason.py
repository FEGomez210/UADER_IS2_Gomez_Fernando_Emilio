import json
import sys

def ejecutar_recuperacion():
    # 1. Validación de la interfaz de comandos: Control de argumentos mínimos
    if len(sys.argv) < 2:
        print("Uso correcto: python getJason.py <ruta_archivo_json> [clave_buscada]")
        sys.exit(1)

    # Asignación del primer parámetro (Ruta del archivo)
    jsonfile = sys.argv[1]

    # 2. Lógica de asignación dinámica de la clave (Requerimiento de Reuso)
    # Si se provee un segundo argumento se utiliza; si no, se aplica el default "token1"
    if len(sys.argv) >= 3:
        jsonkey = sys.argv[2]
    else:
        jsonkey = "token1"

    # 3. Bloque defensivo estructurado (Manejo de errores de infraestructura y datos)
    try:
        # Apertura segura garantizando codificación universal UTF-8
        with open(jsonfile, 'r', encoding='utf-8') as myfile:
            data = myfile.read()
            
        # Parseo del búfer de texto a objeto estructurado
        obj = json.loads(data)

        # 4. Control de existencia de la clave antes de la indexación en memoria
        if jsonkey in obj:
            # Imprime directamente el valor de la clave solicitada
            print(str(obj[jsonkey]))
        else:
            print(f"Error: La clave '{jsonkey}' no se encuentra registrada en el archivo.")
            sys.exit(1)

    except FileNotFoundError:
        print(f"Error de E/S: No se pudo localizar el archivo físico en la ruta: '{jsonfile}'.")
        sys.exit(1)
        
    except json.JSONDecodeError:
        print("Error de Integridad: El archivo provisto no posee una estructura sintáctica JSON válida.")
        sys.exit(1)
        
    except Exception as e:
        print(f"Error inesperado del sistema: {e}")
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_recuperacion()