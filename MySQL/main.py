import mysql.connector
from mysql.connector import connection

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "database_python"
)

cursor = database.cursor()

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS database_python")

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10.2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")

# Insertar elemento a una tabla
cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 185000)")
database.commit()

# Insertar más de un dato
coches = [
    ('Renault', 'Clio', 15000),
    ('Mercedes', 'C', 25000),
    ('Seat', 'Ibiza', 50000)
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()


# Obtener un dato en concreto
cursor.execute("SELECT marca, precio FROM vehiculos")

result = cursor.fetchall()
for coche in result:
    print(coche)

# Eliminar elementos
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Opel'")
database.commit()

# Actualizar
cursor.execute("UPDATE vehiculos SET marca='Leon' WHERE marca = 'Seat'")
database.update()

# Mostrar elementos de una tabla de la base
cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()
for coche in result:
    print(coche)