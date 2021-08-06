# Importar el módulo.
import sqlite3

# Conectar la base
conection = sqlite3.connect('tiendita.db')

# Crear cursos
cursor = conection.cursor()

# Crear una tabla
cursor.execute(
    "CREATE TABLE IF NOT EXISTS productos("+
        "id integer PRIMARY KEY AUTOINCREMENT,"+
        "titulo varchar(255),"+
        "descripcion text,"+
        "precio int(255)"+
    ")"
)

# Guardar cambios
conection.commit()

# Insertar elementos
cursor.execute("INSERT INTO productos VALUES (null, 'Funko de Dory', 'Funko de Dory de Buscando a Nemo', 500)")
conection.commit()

# Borrar registros
cursor.execute("DELETE FROM productos")
conection.commit()

listaProductos = [
    ("Funko de Woody Pixar", "Funko maravilloso del vaquero favorito", 600),
    ("Jugo de manzana", "Rrefrescante jugo Jumex de Manzana", 13),
    ("Juego de cucharas", "10 cucharas para toda la familia", 70),
    ("Sushi", "12 rollos de sushi congelados", 120)
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", listaProductos)
conection.commit()

# Actualizar el precio de un producto
cursor.execute("UPDATE productos SET precio=500 WHERE precio=600")

# Mostrar los datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(producto)

# Cerrar la base
conection.close()