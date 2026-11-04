import app

print("Estudiante: Frazier Gomez Guzman")

admin = app.autenticar("admin", "AdminDemo2700!")
user = app.autenticar("user", "UserDemo2700!")

if admin is None or user is None:
    print("No se pudieron autenticar ambas cuentas.")
else:
    print("\nConsulta como admin:")
    app.consultar_inventario(admin)

    print("\nConsulta como user:")
    app.consultar_inventario(user)

    print("\nCambiar P001 de 10 a 20 como admin:")
    resultado = app.modificar_cantidad(admin, "P001", "20")
    print("Esperado: True | Obtenido:", resultado)
    app.consultar_inventario(admin)

    antes = app.DATOS.read_bytes()

    print("\nIntentar cambiar el producto inexistente P999:")
    resultado = app.modificar_cantidad(admin, "P999", "99")
    print("Esperado: False | Obtenido:", resultado)

    despues = app.DATOS.read_bytes()
    print("Archivo sin cambios tras intentar P999:", antes == despues)

    print("\nInventario final — P001 debe quedar en 20:")
    app.consultar_inventario(admin)