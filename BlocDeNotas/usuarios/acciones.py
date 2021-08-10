from usuarios.usuario import Usuario
import notas.acciones

class Accion:

    def registra(self):
        print("Ingresa los siguientes datos para registrarte")
        nombre = input("¿Cuál es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        email = input("Introduce tu email: ")
        password = input("Ingresa tu contrasena: ")

        us = Usuario(nombre, apellidos, email, password)

        registrado = us.registrar()

        if registrado[0] > 0:
            print(f"El usuario {registrado[1].nombre} ha sido registrado correctamente con email {registrado[1].email}")
        else:
            print("Hubo un problema. El usuario no se ha registrado.")

    def ingresa(self):
        try:
            print("Ingresar al bloc de notas")
            email = input("Introduce tu email: ")
            password = input("Ingresa tu contrasena: ")

            ingresado = Usuario('', '', email, password)

            login = ingresado.identifica()

            if email == login[3]:
                print(f"Bienvenido {login[1]} al bloc. Te registraste el día {login[5]}")
                self.run_system(login)
                exit()
        except:
            print("Aún no te has registrado o tu contraseña es incorrecta")
    
    def run_system(self, usuario):
        print("""
        \n[0] Crear nota\n[1] Mostrar notas\n[2] Eliminar nota\n[3] Salir
        """)

        try:
            opcion = int(input("¿Qué deseas hacer? "))
        except:
            opcion = -1

        ac = notas.acciones.Accion()

        if opcion == 0:
            print("Entra crear")
            ac.crear_nota(usuario)
            print("Sale crear")
        elif opcion == 1:
            print("Entra mostrar")
            ac.mostrar_nota(usuario)
            print("Sale mostrar")
        elif opcion == 2:
            print("entra borrar")
            ac.borrar_nota(usuario)
            print("Sale borrar")
        elif opcion == 3:
            print("Saliendo ...")
            exit()
        else:
            print("Opcion no valida")
        
        self.run_system(usuario)