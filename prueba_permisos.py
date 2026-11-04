import app

print("Estudiante: Frazier Gomez Guzman")

sesion = app.autenticar("user", "UserDemo2700!")

if sesion is None:
    print("No se pudo iniciar sesión como user.")
else:
    antes = app.DATOS.read_bytes()

    print("\nInventario antes de las pruebas:")
    app.consultar_inventario(sesion)

    print("\nPrueba 1: user intenta cambiar P001 a 99")
    resultado = app.modificar_cantidad(sesion, "P001", "99")
    print("Esperado: False | Obtenido:", resultado)

    print("\nPrueba 2: sin sesión intenta cambiar P001 a 99")
    resultado = app.modificar_cantidad(None, "P001", "99")
    print("Esperado: False | Obtenido:", resultado)

    print("\nPrueba 3: consultar sin sesión")
    resultado = app.consultar_inventario(None)
    print("Esperado: False | Obtenido:", resultado)

    print("\nInventario después de las pruebas:")
    app.consultar_inventario(sesion)

    despues = app.DATOS.read_bytes()
    print("\nArchivo sin cambios:", antes == despues)