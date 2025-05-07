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
#Ejemplo de uso yield con send
def generador_con_send():
  while True:
    recibido = yield
    print(f"Valor recibido: {recibido}, tipo: {type(recibido)}")
    if isinstance(recibido, int):
      print(f"El doble del valor recibido es: {recibido * 2}")

gen = generador_con_send()
next(gen)  # Primer next() para iniciar el generador

gen.send(10)
# Salida:
# Valor recibido: 10, tipo: <class 'int'>
# El doble del valor recibido es: 20

gen.send("hola")
# Salida:
# Valor recibido: hola, tipo: <class 'str'>

gen.send([1, 2, 3])
# Salida:
# Valor recibido: [1, 2, 3], tipo: <class 'list'>

gen.close()
#Ejemplo de uso
#Útiles para manejar secuencias grandes sin cargarlas en memoria
