#Secuencia Fibonacci
# La secuencia Fibonacci es una sucesión de números en la que cada número es la suma de los dos anteriores.
#Ejemplo usando yield
from random import seed


def fibonacci(n):
    a,b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
    return a

lista = fibonacci(10)
print(list(lista))  # Imprime: [0, 1, 1, 2, 3, 5, 8]

#Yield devuelve un generador, que es un objeto iterable que se puede recorrer con un bucle for.
#yield permite pausar la ejecución de una función y devolver un valor, y luego reanudarla desde donde se detuvo.
#Metodos de yield
#El método iter() devuelve el objeto iterable
#El método next() devuelve el siguiente valor de la secuencia
#El método send() permite enviar un valor al generador y reanudar su ejecución
#El método throw() permite lanzar una excepción dentro del generador
#El método close() cierra el generador y libera los recursos
#Ejemplo de uso
def generador():
    yield 1
    yield 2
    yield 3

#Ejemplo de uso
lista_generador = generador()
print(next(lista_generador))  # Imprime: 1
print(next(lista_generador))  # Imprime: 2
print(next(lista_generador))  # Imprime: 3

#Ejemplo de uso
#Útiles para manejar secuencias grandes sin cargarlas en memoria
#Otro ejemplo de uso de yield
def contar_hasta(n):
    for i in range(n):
        yield i
#Ejemplo de uso
for numero in contar_hasta(5):
    print(numero)  # Imprime: 0, 1, 2, 3, 4
