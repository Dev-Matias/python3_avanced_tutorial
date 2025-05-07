### **Ejercicio 5:**  
#Crea un decorador que imprima los argumentos de una función antes de ejecutarla.  

def imprimir_argumentos(funcion):
    def envoltura(*args, **kwargs):
        print(f"Argumentos: {args}, {kwargs}")
        return funcion(*args, **kwargs)
    return envoltura

#Ejemplo de uso
@imprimir_argumentos
def suma(a, b):
    return a + b

@imprimir_argumentos
def resta(a, b):
    return a - b

print(suma(3, 5))  # Imprime: Argumentos: (3, 5), {}
print(resta(10, 4))  # Imprime: Argumentos: (10, 4), {}