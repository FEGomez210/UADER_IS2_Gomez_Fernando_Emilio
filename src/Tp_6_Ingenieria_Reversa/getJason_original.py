import json
import sys

# Se asume que el usuario provee al menos la ruta del archivo JSON por consola
jsonfile = sys.argv[1] 

# Limitación original: la clave está fija (hardcoded) en el flujo del programa
jsonkey = 'token1'     

# Apertura y lectura del archivo de datos
with open(jsonfile, 'r') as myfile:
    data = myfile.read()

# Deserialización sintáctica del JSON a un diccionario de Python
obj = json.loads(data)

# Impresión del token recuperado convirtiéndolo a cadena de texto
print(str(obj[jsonkey]))