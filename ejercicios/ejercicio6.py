#Concurrencia Básica (`threading`)
#Tareas en paralelo
#Ejemplo de uso 
from threading import Thread    

def tarea(nombre):
    print(f"Hola {nombre} desde la tarea en segundo plano")

# Crear un hilo
hilo = Thread(target=tarea('Matias'), args=("Hilo 1",))
# Iniciar el hilo
hilo.start()
# Esperar a que el hilo termine
hilo.join()
print("Hola desde el hilo principal")

