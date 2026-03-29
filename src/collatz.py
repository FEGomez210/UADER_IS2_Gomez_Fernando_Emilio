import matplotlib.pyplot as plt

def collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

valores_n = []
iteraciones = []

for i in range(1, 10001):
    valores_n.append(i)
    iteraciones.append(collatz(i))

plt.figure()
plt.plot(valores_n, iteraciones)
plt.xlabel("Número inicial (n)")
plt.ylabel("Iteraciones hasta converger")
plt.title("Conjetura de Collatz (1 a 10000)")
plt.grid()
plt.show()