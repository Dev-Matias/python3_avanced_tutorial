import os
import time
def crear_directorio(directorio):
    os.makedirs(directorio, exist_ok=True)
    print(f"Directorio '{directorio}' creado.")

def crear_archivo(directorio, nombre_archivo):
  with open(os.path.join(directorio, nombre_archivo), 'w') as archivo:
    archivo.write("Este es un archivo de ejemplo.")
    print(f"Archivo '{nombre_archivo}' creado en '{directorio}'.")

def eliminar_archivo(directorio, nombre_archivo):
    ruta_archivo = os.path.join(directorio, nombre_archivo)
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)# Eliminar el archivo
        print(f"Archivo '{nombre_archivo}' eliminado de '{directorio}'.")
    else:
        # Si el archivo no existe, se muestra un mensaje
        print(f"El archivo '{nombre_archivo}' no existe en '{directorio}'.")
        
def listar_archivos(directorio):
    archivos = os.listdir(directorio)
    print(f"Archivos en '{directorio}': {archivos}")

def optener_ruta_archivo(directorio):
    asb_ruta = os.path.abspath(directorio)#Ruta absoluta del directorio
    print(f"Ruta absoluta del directorio '{directorio}': {(asb_ruta)}")


### Ejemplo de uso
crear_archivo("modulos_utiles/ejercicios_modulos", "archivo.txt")
crear_archivo("modulos_utiles/ejercicios_modulos", "archivo2.txt")
time.sleep(2)
eliminar_archivo("modulos_utiles/ejercicios_modulos", "archivo.txt")
crear_directorio("modulos_utiles/ejercicios_modulos")
listar_archivos("modulos_utiles/ejercicios_modulos")
optener_ruta_archivo("modulos_utiles/ejercicios_modulos")