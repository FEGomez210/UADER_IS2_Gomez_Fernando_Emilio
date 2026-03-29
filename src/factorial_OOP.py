import sys

class Factorial:

    def __init__(self):
        pass
    def calcular(self, num):
        if num < 0:
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact
    def run(self, minimo, maximo):
        for i in range(minimo, maximo + 1):
            print(f"{i}! = {self.calcular(i)}")

if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango: ")
else:
    entrada = sys.argv[1]

f = Factorial()

if "-" in entrada:
    partes = entrada.split("-")

    if partes[0] == "":
        inicio = 1
        fin = int(partes[1])
    elif partes[1] == "":
        inicio = int(partes[0])
        fin = 60
    else:
        inicio = int(partes[0])
        fin = int(partes[1])
    f.run(inicio, fin)
else:
    num = int(entrada)
    print(f"{num}! = {f.calcular(num)}")