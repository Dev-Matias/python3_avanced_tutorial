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
"""
uso mas comunes de os
os.getcwd() # Obtener el directorio de trabajo actual
os.chdir("ruta") # Cambiar el directorio de trabajo
os.remove("archivo.txt") # Eliminar un archivo
os.rename("archivo_viejo.txt", "archivo_nuevo.txt") # Renombrar un archivo
os.path.join("directorio", "archivo.txt") # Unir rutas de forma segura
os.path.exists("ruta") # Verificar si una ruta existe
os.path.isfile("archivo.txt") # Verificar si es un archivo
os.path.isdir("directorio") # Verificar si es un directorio
os.path.splitext("archivo.txt") # Separar nombre y extensión
os.path.split("ruta/archivo.txt") # Separar ruta y nombre de archivo
"""
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

## **3. `datetime` – Manejo de fechas y horas `time` Manejo del tiempo**  
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
```python
import time

# 1. time(): Devuelve el número de segundos transcurridos desde la época (punto de inicio del tiempo, generalmente el 1 de enero de 1970 en UTC).
segundos_desde_epoca = time.time()
print(f"Segundos desde la época: {segundos_desde_epoca}")

# 2. ctime([secs]): Convierte un tiempo expresado en segundos desde la época a una cadena que representa la hora local. Si no se proporciona 'secs', utiliza el tiempo actual.
tiempo_local_ahora = time.ctime()
print(f"Tiempo local ahora (ctime): {tiempo_local_ahora}")

tiempo_especifico = 1678886400  # Ejemplo de segundos desde la época
tiempo_local_especifico = time.ctime(tiempo_especifico)
print(f"Tiempo local para {tiempo_especifico} (ctime): {tiempo_local_especifico}")

# 3. sleep(secs): Suspende la ejecución del hilo actual por el número de segundos especificado.
print("Comienza la pausa...")
time.sleep(3)  # Pausa la ejecución por 3 segundos
print("Fin de la pausa.")

# 4. localtime([secs]): Similar a ctime, pero devuelve un objeto struct_time que contiene los componentes del tiempo local (año, mes, día, hora, minuto, segundo, día de la semana, día del año, indicador de horario de verano).
tiempo_local_struct = time.localtime()
print(f"Tiempo local (struct_time): {tiempo_local_struct}")
print(f"Año: {tiempo_local_struct.tm_year}")
print(f"Mes: {tiempo_local_struct.tm_mon}")
print(f"Hora: {tiempo_local_struct.tm_hour}")

# 5. strftime(format[, t]): Convierte una tupla o struct_time representando el tiempo (devuelto por localtime() o gmtime()) a una cadena según el formato especificado. Si no se proporciona 't', utiliza el tiempo actual devuelto por localtime().
formato = "%Y-%m-%d %H:%M:%S"
tiempo_formateado = time.strftime(formato, tiempo_local_struct)
print(f"Tiempo formateado: {tiempo_formateado}")

# Algunos códigos de formato comunes:
# %Y: Año con siglo (ej: 2023)
# %m: Mes como número decimal [01, 12]
# %d: Día del mes como número decimal [01, 31]
# %H: Hora (reloj de 24 horas) como número decimal [00, 23]
# %M: Minuto como número decimal [00, 59]
# %S: Segundo como número decimal [00, 61] (rango incluye segundos bisiestos)
# %a: Abreviatura del nombre del día de la semana (ej: Mon, Tue)
# %A: Nombre completo del día de la semana (ej: Monday, Tuesday)
# %b: Abreviatura del nombre del mes (ej: Jan, Feb)
# %B: Nombre completo del mes (ej: January, February)

# 6. strptime(string[, format]): Analiza una cadena que representa un tiempo según un formato y devuelve un objeto struct_time.
cadena_tiempo = "2024/10/26 15:30:00"
formato_entrada = "%Y/%m/%d %H:%M:%S"
tiempo_analizado = time.strptime(cadena_tiempo, formato_entrada)
print(f"Tiempo analizado (struct_time): {tiempo_analizado}")

# 7. gmtime([secs]): Similar a localtime(), pero devuelve el tiempo en UTC (Tiempo Universal Coordinado).
tiempo_utc = time.gmtime()
print(f"Tiempo UTC (struct_time): {tiempo_utc}")
```
### **Ejercicio:**  
Calcula cuántos días faltan para tu próximo cumpleaños.  
Crea un script que imprima la fecha y hora actual en diferentes formatos.
Crea un script que funcione como cronómetro, mostrando el tiempo transcurrido desde que se inició hasta que se detuvo.
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