import app

print("Estudiante: Frazier Gomez Guzman")

sesion = app.autenticar("admin", "AdminDemo2700!")

if sesion is None:
    print("No se pudo iniciar sesión como admin.")
else:
    casos = [
        ("-1", False),
        ("1001", False),
        ("abc", False),
        ("2.5", False),
        ("", False),
        ("0", True),
        ("1000", True)
    ]

    for entrada, esperado in casos:
        antes = app.DATOS.read_bytes()

        print("\nEntrada:", repr(entrada))
        resultado = app.modificar_cantidad(sesion, "P001", entrada)
        print("Esperado:", esperado, "| Obtenido:", resultado)

        despues = app.DATOS.read_bytes()

        if not esperado:
            print("Archivo sin cambios:", antes == despues)

        productos = app.cargar_inventario()
        for producto in productos:
            if producto["id"] == "P001":
                print("Cantidad guardada de P001:", producto["cantidad"])

    print("\nRestaurando P001 a 10:")
    app.modificar_cantidad(sesion, "P001", "10")
    app.consultar_inventario(sesion)