import mysql.connector

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


