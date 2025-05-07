numero = int(input("Introduce tu edad: "))

try :
    if numero < 0:
        raise ValueError("La edad no puede ser negativa.")
    elif numero > 120:
        raise ValueError("La edad no puede ser mayor a 120.")
    else:
        print(f"Tu edad es: {numero}")
except ValueError as e:
    print(f"Error: {e}")
# En este código, se solicita al usuario que introduzca su edad.
# Luego, se verifica si la edad es negativa o mayor a 120. Si es así, se lanza una excepción ValueError con un mensaje específico.
# Si la edad es válida, se imprime.
