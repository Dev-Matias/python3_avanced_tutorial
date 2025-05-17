import sqlite3

try:
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        departamento TEXT
                    )''')

    # Insertar datos
    cursor.execute("INSERT INTO empleados (nombre, departamento) VALUES (?, ?)", ('Ricardo', 'Ventas'))
    conexion.commit()

    # Leer datos
    cursor.execute("SELECT id, nombre, departamento FROM empleados")
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Departamento: {empleado[2]}")

except sqlite3.Error as e:
    print(f"Error de SQLite: {e}")
    if conexion:
        conexion.rollback()

finally:
    if conexion:
        conexion.close()