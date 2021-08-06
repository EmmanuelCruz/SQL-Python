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

### Crear una tabla

Si quiero crear una tabla de productos, se haría de la siguiente manera tomando en cuenta el lenguaje SQL

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS producto("+
                "id integer PRIMARY KEY AUTOINCREMENT,"+
                "titulo varchar(255),"+
                "descripcion text,"+
                "precio int(255)"+
            ")"
        )

Finalmente, estos cambios aún no forman parte de la base de datos. Para guardar cambios se usa la función _commit_ que no recibe parámetros. 

### Insertar un elemento a una tabla

Para crear una tabla, se utiliza la función execute, al igual que para crear una tabla. Sin embargo, el parámetro de la expresión que recibe es diferente. Esta expresión contiene la inserción a SQL.

                cursor.execute("INSERT INTO tableName VALUES (...)")

Donde _tableName_ es el nombre de la tabla donde se quiere agregar un elemento, y los tres puntos, son los parámetros del elemento a insertar. 

Por otro lado, también es posible insertar elementos en un sólo execute. Es necesario crear una lista con las tuplas que se van a insertar a la tabla. **Importante**: en este caso se utiliza la función _executemany_

                listaProductos = [
                        ("Funko de Woody Pixar", "Funko maravilloso del vaquero favorito", 600),
                        ("Jugo de manzana", "Rrefrescante jugo Jumex de Manzana", 13),
                        ("Juego de cucharas", "10 cucharas para toda la familia", 70),
                        ("Sushi", "12 rollos de sushi congelados", 120)
                ]

                cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", listaProductos)
                conection.commit()

Para guardar los cambios hechos, nuevamente se utiliza la función _commit_ sobre la conexión.

### Mostrar los datos de la base
Como es de suponer, nuevamente se utiliza la función _execute_, pero la instrucción se modifica para obtener elementos.

                cursor.execute("SELECT * FROM tableName")

A su vez, para guardar los elementos resultantes de la consulta, se utiliza la función _fetchall_.

                variable = cursor.fetchall()

Este objeto, es una tupla que contiene todos los elementos almacenados en la tabla _tableName_. Dado que es una tupla, podemos imprir el objeto directamente o también se pueden recorrer sus elementos e imprimir uno a uno. 

Al poder manejarlo como una tupla, también puedo acceder a elementos en una posición específica de la tupla.

                variable[0]
                variable[1]
                variable[2]
                ...

### Eliminar elementos de una tabla

Le eliminación también está basa en la expresión SQL para la eliminación. Dependiendo de la sintaxis o indicación en la consulta, se pueden eliminar valores específicos. En general, para borrar los elementos de una tabla se usa la siguiente expresión

                cursor.execute("DELE FROM productos")

Es importante saber que para que los cambios se vean reflejados, es necesario utilizar la función _commit_. En caso de no usarla, la base no sufrirá ningún cambio.

### Actualizar elementos de una tabla

¡Oh sorpresa! Adivinaste, utilizamos _execute_ con la expresión de actualización de SQL.

                cursor.execute("UPDATE tableName SET atributo=500 WHERE atributo=600")

En la consulta anterior, actualizamos el atributo a 600 de todos aquellos que tengan valor 500 en su atributo dentro de la tabla _tableName_.
