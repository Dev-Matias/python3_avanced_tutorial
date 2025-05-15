# **Tutorial Avanzado de Python con Ejercicios Prácticos** 🚀🐍  

Ahora que ya conoces los fundamentos, profundicemos en conceptos más avanzados de Python: **programación orientada a objetos (OOP), manejo de excepciones, módulos, generadores, decoradores y concurrencia básica**.  (**Generado con DeepSeek**)

---

## **1. Programación Orientada a Objetos (OOP)**  
Python soporta **clases, herencia, polimorfismo y encapsulamiento**.  

### **Ejemplo: Clase `Persona`**  
```python
class Persona:
    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre  # Atributo
        self.edad = edad

    def presentarse(self):  # Método
        return f"Soy {self.nombre} y tengo {self.edad} años."

# Uso
persona1 = Persona("Ana", 30)
print(persona1.presentarse())
```
**Salida:**  
```
Soy Ana y tengo 30 años.
```

### **Herencia**  
```python
class Estudiante(Persona):  # Hereda de Persona
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llama al constructor de Persona
        self.carrera = carrera

    def presentarse(self):  # Sobrescribe el método
        return f"{super().presentarse()} Estudio {self.carrera}."

estudiante1 = Estudiante("Luis", 22, "Informática")
print(estudiante1.presentarse())
```
**Salida:**  
```
Soy Luis y tengo 22 años. Estudio Informática.
```

### **Ejercicio 1:**  
Crea una clase `Rectangulo` con métodos para calcular su área y perímetro.  
**Resuelto** [ejercicio1.py](./ejercicios/ejercicio1.py)  
---

## **2. Manejo de Excepciones (`try-except`)**  
Evita que tu programa se detenga por errores.  

### **Ejemplo:**  
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error: División por cero!")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Todo salió bien.")
finally:
    print("Fin del bloque try-except.")
```
**Salida:**  
```
¡Error: División por cero!
Fin del bloque try-except.
```

### **Ejercicio 2:**  
Pide al usuario un número y maneja el error si ingresa texto.  
**Resuelto** [ejercicio2.py](./ejercicios/ejercicio2.py)
---

## **3. Módulos y Paquetes**  
### **Crear un módulo (`mi_modulo.py`)**  
```python
def saludo(nombre):
    return f"Hola, {nombre}!"

PI = 3.1416
```

### **Importar el módulo**  
```python
import mi_modulo
print(mi_modulo.saludo("Carlos"))  # Hola, Carlos!
print(mi_modulo.PI)                # 3.1416
```
### **Paquetes**
Un paquete es una colección de módulos.
Para crear un paquete, crea un directorio con un archivo `__init__.py` y coloca tus módulos dentro.
`__init__.py` archivo especial __init__.py (puede estar vacío). Permite agrupar módulos relacionados
```bash
mkdir mi_paquete
cd mi_paquete
touch __init__.py  # Indica que es un paquete
```
```python
# mi_paquete/__init__.py
from .mi_modulo import saludo, PI  # Importa funciones y variables
```
```python
# mi_paquete/mi_modulo.py
def saludo(nombre):
    return f"Hola, {nombre}!"
PI = 3.1416
```
```python
# main.py
from mi_paquete import saludo, PI
print(saludo("Carlos"))  # Hola, Carlos!
print(PI)                # 3.1416
```
### **Ejercicio 3:**  
Crea un paquete llamado `matematicas` con un módulo `operaciones.py` que incluya funciones para sumar y multiplicar.  
**Resuelto** [ejercicio3.py](./ejercicios/ejercicio3.py)  

---

## **4. Generadores (`yield`)**  
Útiles para manejar secuencias grandes sin cargarlas en memoria.  

### **Ejemplo:**  
```python
def generador_pares(limite):
    for i in range(0, limite, 2):
        yield i  # Devuelve valores uno a uno

pares = generador_pares(10)
print(list(pares))  # [0, 2, 4, 6, 8]
```

### **Ejercicio 4:**  
Crea un generador que devuelva los números de Fibonacci hasta un límite.  
**Resuelto** [ejercicio4.py](./ejercicios/ejercicio4.py)  

---

## **5. Decoradores**  
Modifican el comportamiento de una función sin cambiar su código.  

### **Ejemplo: Decorador para medir tiempo**  

```python
import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        # :.2f dar formato para mostrar un flotante, dos decgitos despues del punto, puede ser :.nf *n decimales*
        print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def suma_lenta(a, b):
    time.sleep(1)  # Simula procesamiento lento
    return a + b

print(suma_lenta(5, 3))
```
**Salida:**  
```
Tiempo de ejecución: 1.00 segundos
8
```
# Tips
descripción y el uso de `*args` y `**kwargs` en Python 3:
**`*args`**

- **Descripción:** `*args` se utiliza en la definición de una función para pasar un número variable de argumentos posicionales. Internamente, Python empaqueta estos argumentos en una tupla.
- **Uso:** Es útil cuando no sabes de antemano cuántos argumentos posicionales se pasarán a una función. Permite que la función reciba cualquier número de argumentos y los procese de manera flexible.

Python

```python
def mi_funcion_args(*args):
    for arg in args:
        print(arg)

mi_funcion_args("Hola", 10, 3.14, True)
# Salida:
# Hola
# 10
# 3.14
# True
```

**`**kwargs`**

- **Descripción:** `**kwargs` se utiliza en la definición de una función para pasar un número variable de argumentos con nombre (palabras clave). Internamente, Python empaqueta estos argumentos en un diccionario, donde las claves son los nombres de los argumentos y los valores son sus respectivos valores.
- **Uso:** Es útil cuando necesitas pasar un conjunto de parámetros con nombre a una función, sin tener que definir cada parámetro individualmente en la firma de la función.

Python

```python
def mi_funcion_kwargs(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mi_funcion_kwargs(nombre="Ana", edad=30, ciudad="Buenos Aires")
# Salida:
# nombre: Ana
# edad: 30
# ciudad: Buenos Aires
```

**En resumen:**

- `*args` permite pasar un número variable de argumentos **posicionales** a una función, que se reciben como una **tupla**.
- `**kwargs` permite pasar un número variable de argumentos con **nombre (palabra clave)** a una función, que se reciben como un **diccionario**.

Ambos son herramientas poderosas para crear funciones más flexibles y genéricas en Python.
### **Ejercicio 5:**  
Crea un decorador que imprima los argumentos de una función antes de ejecutarla.  
**Resuelto** [ejercicio5.py](./ejercicios/ejercicio5.py)

---

## **6. Concurrencia Básica (`threading`)**  
Ejecuta tareas en paralelo.  

### **Ejemplo:**  
```python
import threading

def tarea(nombre):
    print(f"Iniciando hilo: {nombre}")

hilo1 = threading.Thread(target=tarea, args=("Hilo 1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo 2",))

hilo1.start()
hilo2.start()

hilo1.join()  # Espera a que termine
hilo2.join()
```
**Salida (puede variar):**  
```
Iniciando hilo: Hilo 1
Iniciando hilo: Hilo 2
```

### **Ejercicio 6:**  
Crea dos hilos: uno que imprima números pares y otro impares del 1 al 10.  
**Resuelto** [ejercicio6.py](./ejercicios/ejercicio6.py)
---
# Instalar dependencias usando pip y creando entornos virtuales

- instalar en ubuntu y derivadas

```bash
sudo apt install python3-pip
```

- Entornos virtuales para instalar y manejar dependencias

```bash
mkdir python_proyecto
cd python_proyecto
python3 -m venv .venv
```

- Activar entorno virtual

```bash
source .venv/bin/activate
```
## **7. Proyecto Avanzado: API con Flask**  
Crea un servidor web básico:  
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Bienvenido a mi API!"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    app.run(debug=True)
```
Ejecuta y visita:  
- `http://127.0.0.1:5000/`  
- `http://127.0.0.1:5000/saludo/Python`  

---
## **Consumir API REST**  
```python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)  # 200
print(response.json())  # Muestra el contenido JSON
```
---
## **8. Proyecto Avanzado: Rick and Morty game**  
Crea un juego de texto donde el usuario interactúe con personajes de Rick and Morty. Documentacion de la API:
- **[Rick and Morty API](https://rickandmortyapi.com/documentation)** 
```bash
URL="https://rickandmortyapi.com/api/character"
```
**Rsuelto** [ejercicio7.py](./ejercicios/ejercicio7.py)
## **Recursos Avanzados**  
- **[Python OOP (Real Python)](https://realpython.com/python3-object-oriented-programming/)**  
- **[Decoradores (GeekForGeeks)](https://www.geeksforgeeks.org/decorators-in-python/)**  
- **[Concurrencia (Python Docs)](https://docs.python.org/3/library/threading.html)**  

¡Domina estos conceptos y llevarás tu Python al siguiente nivel! 🔥