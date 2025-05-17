import sys

print("Arguemento 1:", sys.argv[1])
print("Arguemento 2:", sys.argv[2])

#Version de Python
print("Version de Python:", sys.version)

#Argumentos de la linea de comandos
print("Argumentos de la linea de comandos:", sys.argv)

#Sumar dos argumentos pasados por la linea de comandos
def sumar_argumentos(arg1, arg2):
    try:
        resultado = int(arg1) + int(arg2)
        print(f"La suma de {arg1} y {arg2} es: {resultado}")
    except ValueError:
        print("Error: Los argumentos deben ser números enteros.")

sumar_argumentos(sys.argv[1], sys.argv[2])
#SAlir del script
print("Saliendo del script")
sys.exit(0)