from usuarios import acciones

print("""
[0] Registrarte
[1] Login
""")

opcion = -1

try:
    opcion = int(input("Eligue una opción: "))
except Exception:
    print("Opción no válida")

usuario_accion = acciones.Accion()

if opcion == 0:
    usuario_accion.registra()
elif opcion == 1:
    usuario_accion.ingresa()
else:
    print("Opción no definida")