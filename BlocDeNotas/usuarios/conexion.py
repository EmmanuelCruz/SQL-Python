import mysql.connector

def conectar():

    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "data_base"
    )

    cursor = database.cursor(buffered=True)

    return database, cursor