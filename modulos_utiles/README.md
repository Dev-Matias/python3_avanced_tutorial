# **Módulos más útiles de la librería estándar de Python** 📚  

La biblioteca estándar de Python incluye módulos poderosos para tareas comunes. Aquí tienes una lista de los más importantes con ejemplos y ejercicios.  

---

## **1. `os` – Interacción con el sistema operativo**  
**Descripción:** Maneja archivos, directorios y variables de entorno.  

### **Ejemplo:**  
```python
import os

# Crear un directorio
os.mkdir("nueva_carpeta")  

# Listar archivos en el directorio actual
print(os.listdir("."))  

# Obtener la ruta absoluta
print(os.path.abspath("nueva_carpeta"))  
```

### **Ejercicio:**  
Crea un script que liste todos los archivos `.txt` en un directorio dado.  

---

## **2. `sys` – Funciones del sistema**  
**Descripción:** Accede a variables y funciones del intérprete Python.  

### **Ejemplo:**  
```python
import sys

# Argumentos de la línea de comandos
print("Argumentos:", sys.argv)  

# Versión de Python
print("Versión:", sys.version)  

# Salir del programa
sys.exit(0)  
```

### **Ejercicio:**  
Haz un script que sume dos números pasados como argumentos (`python script.py 5 3` → `8`).  

---

## **3. `datetime` – Manejo de fechas y horas**  
**Descripción:** Trabaja con fechas, horas y diferencias de tiempo.  

### **Ejemplo:**  
```python
from datetime import datetime, timedelta

# Fecha actual
ahora = datetime.now()
print("Hoy:", ahora.strftime("%d/%m/%Y"))  

# Sumar 5 días
futuro = ahora + timedelta(days=5)
print("En 5 días:", futuro.day)  
```

### **Ejercicio:**  
Calcula cuántos días faltan para tu próximo cumpleaños.  

---

## **4. `json` – Manipulación de JSON**  
**Descripción:** Convierte entre JSON y diccionarios de Python.  

### **Ejemplo:**  
```python
import json

# Convertir diccionario a JSON
datos = {"nombre": "Ana", "edad": 25}
json_str = json.dumps(datos)  
print(json_str)  

# Leer JSON desde archivo
with open("datos.json", "w") as f:
    json.dump(datos, f)  
```

### **Ejercicio:**  
Crea un archivo `usuarios.json` con una lista de diccionarios (nombre, email).  

---

## **5. `random` – Generación de números aleatorios**  
**Descripción:** Útil para simulaciones, juegos y pruebas.  

### **Ejemplo:**  
```python
import random

# Entero aleatorio entre 1 y 10
print(random.randint(1, 10))  

# Escoger un elemento al azar
lista = ["a", "b", "c"]
print(random.choice(lista))  

# Barajar una lista
random.shuffle(lista)  
print(lista)  
```

### **Ejercicio:**  
Simula 100 lanzamientos de un dado y cuenta cuántas veces sale el número 6.  

---

## **6. `re` – Expresiones regulares**  
**Descripción:** Búsqueda y manipulación de texto avanzado.  

### **Ejemplo:**  
```python
import re

# Buscar un patrón
texto = "Python 3.10 es rápido"
coincidencia = re.search(r"\d+\.\d+", texto)  
print(coincidencia.group())  # 3.10  

# Reemplazar texto
nuevo_texto = re.sub(r"rápido", "eficiente", texto)  
print(nuevo_texto)  
```

### **Ejercicio:**  
Valida si un string es un email válido (ej: `usuario@dominio.com`).  

---

## **7. `collections` – Estructuras de datos avanzadas**  
**Descripción:** Contenedores especializados como `defaultdict`, `Counter`, etc.  

### **Ejemplo:**  
```python
from collections import Counter, defaultdict

# Contar elementos
lista = ["a", "b", "a", "c", "b"]
print(Counter(lista))  # {"a": 2, "b": 2, "c": 1}  

# Diccionario con valor por defecto
d = defaultdict(int)
d["clave"] += 1  
print(d["clave"])  # 1  
```

### **Ejercicio:**  
Cuenta la frecuencia de palabras en un texto (ignorando mayúsculas/minúsculas).  

---

## **8. `subprocess` – Ejecutar comandos del sistema**  
**Descripción:** Corre comandos de terminal desde Python.  

### **Ejemplo:**  
```python
import subprocess

# Ejecutar comando (Linux/Mac)
resultado = subprocess.run(["ls", "-l"], capture_output=True, text=True)  
print(resultado.stdout)  

# En Windows: subprocess.run(["dir"], shell=True)  
```

### **Ejercicio:**  
Crea un script que liste los procesos en ejecución (usando `ps aux` en Linux o `tasklist` en Windows).  

---

## **9. `argparse` – Parseo de argumentos CLI**  
**Descripción:** Crea interfaces de línea de comandos profesionales.  

### **Ejemplo:**  
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nombre", help="Tu nombre")  
args = parser.parse_args()  

if args.nombre:
    print("Hola,", args.nombre)  
```
**Uso:**  
```bash
python script.py --nombre Ana  
```

### **Ejercicio:**  
Haz un script que acepte `--archivo` y cuente sus líneas.  

---

## **10. `sqlite3` – Bases de datos SQLite**  
**Descripción:** Base de datos ligera sin servidor.  

### **Ejemplo:**  
```python
import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER)")  

# Insertar datos
cursor.execute("INSERT INTO usuarios VALUES (?, ?)", ("Ana", 25))  
conn.commit()  

conn.close()  
```

### **Ejercicio:**  
Crea una DB de tareas pendientes (`id`, `tarea`, `completada`).  

---

## **Bonus: Otros módulos útiles**  
| Módulo          | Uso                              |  
|----------------|----------------------------------|  
| `math`         | Funciones matemáticas (`sqrt`, `sin`) |  
| `csv`          | Leer/escribir archivos CSV       |  
| `logging`      | Registro de eventos (logs)       |  
| `zipfile`      | Manipular archivos ZIP           |  
| `threading`    | Programación concurrente         |  

---

### **Ejercicio Final:**  
Combina `os`, `json` y `datetime` para crear un script que:  
1. Lea un archivo JSON con tareas.  
2. Genere un reporte en un archivo `reporte_<fecha>.txt`.  
3. Muestre cuántas tareas están completadas.  

¡Domina estos módulos y tendrás un control total sobre Python! 🚀