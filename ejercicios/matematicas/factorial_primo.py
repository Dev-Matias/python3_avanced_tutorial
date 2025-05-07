#Factorial multiplicación sussesiva de un número hacia abajo hasta 1
def factorial(n):
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)#Funcion recursiva para calcular el factorial de un número

#Funcion para determinar si un número es primo
# Un número es primo si es mayor que 1 y no tiene divisores positivos distintos de 1 y sí mismo
# Un número primo es un número natural mayor que 1 que no tiene divisores positivos distintos de 1 y sí mismo.
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True