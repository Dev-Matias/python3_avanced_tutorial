#Concurrencia Básica (`threading`)
#Tareas en paralelo
#Ejemplo de uso 
from threading import Thread    
import time
def tarea(nombre):
    print(f"Hola {nombre} desde la tarea en segundo plano")

def tarea2(nombre): 
    # Simulación de una tarea que toma tiempo
    time.sleep(2)
    print(f"Hola {nombre} desde la tarea en segundo plano")
# Crear un hilo
hilo = Thread(target=tarea, args=("Hilo 1",))
hilo2 = Thread(target=tarea('Tarea 2'))
hilo3 = Thread(target=tarea2, args=("Hilo 3 que toma tiempo",))
# Iniciar el hilo
hilo3.start()
hilo.start()
hilo2.start()
# Esperar a que el hilo termine
hilo.join()
hilo3.join()
hilo2.join()
print("Hola desde el hilo principal")

