import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 40 
inicio = time.time()
resultado = fib(n)
fin = time.time()

print(f"Fib({n}) = {resultado}")
print(f"Tiempo en Python: {fin - inicio:.6f} segundos")

