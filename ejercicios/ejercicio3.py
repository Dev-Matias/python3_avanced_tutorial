# Se importan las funciones de suma, resta, multiplicación y división del archivo matematicas/operaciones.py
from matematicas.operaciones import sumar, restar, multiplicar, dividir

print("Ejercicio 3: Importar funciones de otro archivo")
# Solicitar al usuario dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones
suma_resultado = sumar(num1, num2)
resta_resultado = restar(num1, num2)
multiplicacion_resultado = multiplicar(num1, num2)
division_resultado = dividir(num1, num2)

# Mostrar los resultados
print(f"Suma: {suma_resultado}")
print(f"Resta: {resta_resultado}")
print(f"Multiplicación: {multiplicacion_resultado}")
print(f"División: {division_resultado}")
