# SQLite con Python
## Emmanuel Cruz Hernández

----

## Descripción

Manejo de bases de datos en Python utilizando SQLite.

----

## Sobre SQLite

SQLite es un módulo que ya está instalado con Python, por lo que no es necesario instalar otro módulo o paquete. 

Para poder utilizar sqlite, se debe importar el módulo

        import sqlite3

Para hacer la conexión a la base, basta con utilizar la función _connect_. Esta recibe un parámetro, que es el nombre de la base de datos, con extensión ***db***.

        conection = sqlite3.connect('name.db')

Hasta este momento, ya se tiene la conexión a una base de datos vacía. Para poder manipularla, es necesario tener un cursor de apoyo para crear tablas, eliminar tablas, entre otras operaciones. SQLite ya cuenta con una función que provee un cursor para realizar todas estas operaciones.

        cursor = conection.cursor()

Finalmente, para expresar una instrucción propia de SQL, se utiliza una función llamada execute, que recibe como parámetro un String con la consulta o las operaciones que se harán hacia la base.

        cursor.execute("SQL expresion")

Por ejemplo, si quiero crear una tabla de productos, se haría de la siguiente manera tomando en cuenta el lenguaje SQL

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS producto("+
                "id integer PRIMARY KEY AUTOINCREMENT,"+
                "titulo varchar(255),"+
                "descripcion text,"+
                "precio int(255)"+
            ")"
        )

Finalmente, estos cambios aún no forman parte de la base de datos. Para guardar cambios se usa la función _commit_ que no recibe parámetros. 