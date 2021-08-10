import usuarios.conexion as conexion

connect = conexion.conectar()
databse = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    def guardar(self):
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        databse.commit()

        return [cursor.rowcount, self]
    
    def listar_notas(self):
        sql = f"SELECT * FROM notas WHERE usuario_id={self.usuario_id}"

        cursor.execute(sql)
        listado = cursor.fetchall()

        return listado
    
    def eliminar_nota(self, titulo):
        sql = f"DELETE FROM notas WHERE usuario_id={self.usuario_id} AND titulo LIKE '%{titulo}%'"

        cursor.execute(sql)
        databse.commit()

        return [cursor.rowcount, self]