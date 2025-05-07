#Secuencia Fibonacci
# La secuencia Fibonacci es una sucesión de números en la que cada número es la suma de los dos anteriores.
#Ejemplo usando yield
def fibonacci(n):
    a,b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
    return a
fibonacci(10)
#Yield devuelve un generador, que es un objeto iterable que se puede recorrer con un bucle for.
#Útiles para manejar secuencias grandes sin cargarlas en memoria