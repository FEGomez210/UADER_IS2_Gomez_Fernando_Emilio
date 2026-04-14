"""
TP2 Arquitectura
Materia: Ingeniería de Software 2
Autor: Fernando Emilio Gómez
Profesor: Dr. Pedro E. Colla
Ayudante: Lic. Lucía Blanc
Descripción: Evaluador de expresiones en notación polaca inversa (RPN)
Universidad: UADER-FCyt C.D.U.
"""

import math
import sys


class RPNError(Exception):
    """Error de evaluación RPN: encapsula fallas de parsing, pila y operaciones."""

class RPN:
    """
    Evaluador RPN basado en pila.

    Diseño:
    - Modelo stack-based (LIFO)
    - Separación entre operaciones binarias y unarias
    - Extensible mediante nuevos tokens en run()
    """

    def __init__(self):
        """Inicializa pila de ejecución y 10 registros de memoria."""
        self.s = []
        self.m = [0.0] * 10

    def push(self, x):
        """Inserta valor en la pila (normalizado a float)."""
        self.s.append(float(x))

    def pop(self):
        """Extrae el tope de la pila."""
        if not self.s:
            raise RPNError("pila insuficiente")
        return self.s.pop()

    def bin(self, f):
        """Ejecuta operación binaria sobre la pila."""
        if len(self.s) < 2:
            raise RPNError("pila insuficiente")
        b, a = self.pop(), self.pop()
        return f(a, b)

    def run(self, expr):
        """Evalúa una expresión RPN."""
        for t in expr.split():

            if t in "+-*/":
                if t == "+":
                    self.push(self.bin(lambda a, b: a + b))
                elif t == "-":
                    self.push(self.bin(lambda a, b: a - b))
                elif t == "*":
                    self.push(self.bin(lambda a, b: a * b))
                elif t == "/":

                    def div(a, b):
                        if b == 0:
                            raise RPNError("division por cero")
                        return a / b

                    self.push(self.bin(div))

            elif t == "dup":
                if not self.s:
                    raise RPNError("pila insuficiente")
                self.push(self.s[-1])

            elif t == "swap":
                if len(self.s) < 2:
                    raise RPNError("pila insuficiente")
                self.s[-1], self.s[-2] = self.s[-2], self.s[-1]

            elif t == "drop":
                self.pop()

            elif t == "clear":
                self.s.clear()

            elif t == "p":
                self.push(math.pi)

            elif t == "e":
                self.push(math.e)

            elif t == "j":
                self.push((1 + 5 ** 0.5) / 2)

            elif t == "sqrt":
                self.push(math.sqrt(self.pop()))

            elif t == "log":
                self.push(math.log10(self.pop()))

            elif t == "ln":
                self.push(math.log(self.pop()))

            elif t == "ex":
                self.push(math.exp(self.pop()))

            elif t == "10x":
                self.push(10 ** self.pop())

            elif t == "yx":
                self.push(self.bin(lambda a, b: a ** b))

            elif t == "1/x":
                x = self.pop()
                if x == 0:
                    raise RPNError("division por cero")
                self.push(1 / x)

            elif t == "chs":
                self.push(-self.pop())

            elif t == "sin":
                self.push(math.sin(math.radians(self.pop())))

            elif t == "cos":
                self.push(math.cos(math.radians(self.pop())))

            elif t == "tg":
                self.push(math.tan(math.radians(self.pop())))

            elif t == "asin":
                self.push(math.degrees(math.asin(self.pop())))

            elif t == "acos":
                self.push(math.degrees(math.acos(self.pop())))

            elif t == "atg":
                self.push(math.degrees(math.atan(self.pop())))

            elif t == "sto":
                i = int(self.pop())
                if not 0 <= i <= 9:
                    raise RPNError("memoria invalida")
                self.m[i] = self.pop()

            elif t == "rcl":
                i = int(self.pop())
                if not 0 <= i <= 9:
                    raise RPNError("memoria invalida")
                self.push(self.m[i])

            else:
                try:
                    self.push(float(t))
                except Exception as exc:
                    raise RPNError(f"token invalido: {t}") from exc

        if len(self.s) != 1:
            raise RPNError("la pila no termino en un unico valor")

        return self.pop()


def main():
    """Entrada del programa."""
    try:
        expr = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input()
        r = RPN().run(expr)
        print(int(r) if r.is_integer() else r)
    except RPNError as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()
