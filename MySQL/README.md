# MySQL con Python
## Emmanuel Cruz Hernández

----

#### Descripción

Manejo de bases de datos con MySQL en Python.

---- 

## Sobre MySQL

MySQL es otro manejador de bases de datos que se puede manejar con Python, entre otras funciones. Para instalar el módulo, se requiere instalar Xampp o Wampserver. 

El módulo para manejar MySQL con Python también se debe descargar con la siguiente instrucción:

        pip install mysql-connector-python

Para hacer uso del módulo, se importa con la instrucción siguiente

        import mysql

En particular, se va a utilizar el conector de mysql, por lo que también podríamos importar de la siguiente manera

        import mysql.connector

Para la creación de la base de datos, se utiliza la función _connect_, que está implementada para un connector. Este recibe algunos parámetros
* host: el host donde se va a conectar la base de datos. Para proyectos locales es _localhost_
* user: el nombre de usuario, que por default, es _root_.
* password: la contraseña hacia la base, por default es una cadena vacía.
* database: una referencia a la base de datos asociada.

Es importante mencionar que el último parámetro puede no pasarse, ya que la base de datos se puede crear directamente desde Python.

### Crear una base de datos

Para crear una base de datos se utiliza la función _execute_, implementado para un **cursor** que recibe como parámetro una cadena con la instrucción en SQL de la consulta que se quiere realizar. En particular, para crear una base de datos

        cursor = database.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS databaseName")

Notése que una vez ejecutado el programa, se mostrará la nueva base creada en _phpMyAdmin_.

![base](Base.PNG)

### Crear una tabla

Para crear una tabla nuevamente se utiliza la función _execute_, son la instrucción en SQL para la creación de una tabla. Por ejemplo, si quiero crear una tabla de vehículos, lo puedo hacer de la siguiente forma, utilizando el cursor.

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehiculos(
                id int(10) auto_increment not null,
                marca varchar(40) not null,
                modelo varchar(40) not null,
                precio float(10.2) not null,
                CONSTRAINT pk_vehiculo PRIMARY KEY (id)
            )
        """)

**NOTA**: Esta sintaxis también es válida para [SQLite](https://github.com/EmmanuelCruz/SQL-Python/tree/master/SQLite).

Si se corre el programa, podemos notar que en _phpMyAdmin_ ya se encuentra creada la tabla en la base de datos.

![tabla](Tabla.PNG)