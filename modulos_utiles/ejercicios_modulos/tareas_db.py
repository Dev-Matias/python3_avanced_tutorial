import sqlite3


try:
    conexion = sqlite3.connect('mis_tareas.db')
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarea TEXT NOT NULL,
                        completado BOOLEAN DEFAULT FALSE
                    )''')
except sqlite3.Error as e:
        print(f"Fallo al crear la DB Error SQL: {e}")    
        if conexion:
            conexion.rollback()

def crear_tarea(tarea,completado):
    # Insertar datos
    cursor.execute("INSERT INTO tareas (tarea, completado) VALUES (?, ?)", (tarea, completado))
    conexion.commit()

def leer_tarea():
        # Leer datos
    cursor.execute("SELECT id, tarea, completado FROM tareas")
    tareas = cursor.fetchall()
    for tarea in tareas:
        print(f"ID: {tarea[0]}, Tarea A realizar: {tarea[1]}, Completado?: {tarea[2]}")

    

crear_tarea("Crear Mas Apps y juegos","FALSE")
crear_tarea("Practicar Flutter","FALSE")
crear_tarea("Practicar Python3","TRUE")
leer_tarea()
