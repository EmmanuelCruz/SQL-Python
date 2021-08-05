# Importar el módulo.
import sqlite3

# Conectar la base
conection = sqlite3.connect('tiendita.db')

# Crear cursos
cursor = conection.cursor()

# Crear una tabla
cursor.execute(
    "CREATE TABLE IF NOT EXISTS producto("+
        "id integer PRIMARY KEY AUTOINCREMENT,"+
        "titulo varchar(255),"+
        "descripcion text,"+
        "precio int(255)"+
    ")"
)

# Guardar cambios
conection.commit()

# Cerrar la base
conection.close()