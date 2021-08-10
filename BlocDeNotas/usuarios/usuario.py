import datetime
import hashlib
import usuarios.conexion as conexion

conexion = conexion.conectar()
database = conexion[0]
cursor = conexion[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"

        cifrador = hashlib.sha256()
        cifrador.update(self.password.encode('utf8'))

        usuario = (self.nombre, self.apellidos, self.email, cifrador.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identifica(self):
        sql = "SELECT * FROM usuarios WHERE email=%s AND password = %s"

        cifrador = hashlib.sha256()
        cifrador.update(self.password.encode('utf8'))

        usuario = (self.email, cifrador.hexdigest())

        cursor.execute(sql, usuario)
        user = cursor.fetchone()

        return user