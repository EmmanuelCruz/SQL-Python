from notas.nota import Nota

class Accion:

    def crear_nota(self, usuario):
        print("Entra crear nota Acciones")
        titulo = input("Titulo de nota: ")
        descripcion = input("Nota: ")

        nota_data = Nota(usuario[0], titulo, descripcion)

        nueva = nota_data.guardar()

        if nueva[0] > 0:
            print(f"La nota {titulo} se ha guardado correctamente")
        else:
            print(f"No se ha guardado la nota. Lo siento {usuario[1]}")
    
    def mostrar_nota(self, usuario):
        notas = Nota(usuario[0])

        listado = notas.listar_notas()

        for mi_nota in listado:
            print(f"""
            ***************** {mi_nota[2]} *****************
            {mi_nota[3]}
            ************************************************
            """)
    
    def borrar_nota(self, usuario):
        titulo = input("Introduce el titulo de la nota a borrar: ")

        aux = Nota(usuario[0], titulo)
        eliminada = aux.eliminar_nota(titulo)

        if eliminada[0] > 0:
            print(f"Se ha borrado la nota {titulo}")
        else:
            print("No se ha borrado la nota")