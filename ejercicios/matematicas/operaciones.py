def sumar(a,b):
    return a + b
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
def potencia(a,b):
    return a ** b
def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return a ** 0.5
def factorial(n):
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True