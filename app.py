"""Inventario académico — COMP2700."""
import json
from pathlib import Path
from datetime import datetime
from seguridad import verificar_clave

RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "inventario.json"
USUARIOS = RAIZ / "usuarios.json"
LOG = RAIZ / "auditoria.jsonl"


def cargar_inventario():
    try:
        contenido = DATOS.read_text(encoding="utf-8")
        return json.loads(contenido)
    except FileNotFoundError:
        print("Error: no se encontró inventario.json. Restaure el archivo.")
    except json.JSONDecodeError:
        print("Error: inventario.json no contiene JSON válido. Restaure el archivo.")
    except (OSError, UnicodeError):
        print("Error: no se pudo leer inventario.json.")

    return None


def guardar_inventario(productos):
    try:
        DATOS.write_text(
            json.dumps(productos, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        return True
    except OSError:
        print("Error: no se pudo guardar el inventario.")
        return False


def registrar_evento(usuario, accion, resultado, **detalles):
    evento = {
        "fecha_hora": datetime.now().astimezone().isoformat(),
        "usuario": usuario,
        "accion": accion,
        "resultado": resultado
    }

    for campo in ("producto", "anterior", "nueva"):
        if campo in detalles:
            evento[campo] = detalles[campo]

    try:
        with LOG.open("a", encoding="utf-8") as archivo:
            archivo.write(json.dumps(evento, ensure_ascii=False) + "\n")
        return True
    except OSError:
        print("Error: no se pudo registrar el evento en auditoria.jsonl.")
        return False


def autenticar(nombre, clave):
    try:
        usuarios = json.loads(USUARIOS.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        print("Error: no se pudo leer el archivo de usuarios.")
        return None

    for usuario in usuarios:
        if usuario["usuario"] == nombre:
            if verificar_clave(usuario["hash"], clave):
                registrar_evento(nombre, "login", "exitoso")
                return {"usuario": nombre, "rol": usuario["rol"]}
            break

    registrar_evento(nombre, "login", "fallido")
    print("Credenciales incorrectas.")
    return None


def sesion_valida(sesion):
    return (
        isinstance(sesion, dict)
        and isinstance(sesion.get("usuario"), str)
        and bool(sesion.get("usuario"))
        and sesion.get("rol") in ("admin", "user")
    )


def consultar_inventario(sesion):
    if not sesion_valida(sesion):
        print("Acceso rechazado: debe iniciar sesión.")
        registrar_evento("sin_sesion", "consultar", "rechazado_sin_sesion")
        return False

    productos = cargar_inventario()
    if productos is None:
        return False

    for producto in productos:
        print(producto["id"], producto["nombre"], producto["cantidad"])

    return True


def modificar_cantidad(sesion, identificador, entrada):
    if not sesion_valida(sesion):
        print("Modificación rechazada: debe iniciar sesión.")
        registrar_evento(
            "sin_sesion", "modificar", "rechazado_sin_sesion",
            producto=identificador
        )
        return False

    if sesion["rol"] != "admin":
        print("Modificación rechazada: solo admin puede modificar cantidades.")
        registrar_evento(
            sesion["usuario"], "modificar", "rechazado_por_permisos",
            producto=identificador
        )
        return False

    try:
        cantidad = int(entrada)
    except (ValueError, TypeError):
        print("Cantidad inválida: escriba un número entero entre 0 y 1000.")
        return False

    if cantidad < 0 or cantidad > 1000:
        print("Cantidad inválida: el número debe estar entre 0 y 1000.")
        return False

    productos = cargar_inventario()
    if productos is None:
        return False

    for producto in productos:
        if producto["id"] == identificador:
            anterior = producto["cantidad"]
            producto["cantidad"] = cantidad

            if not guardar_inventario(productos):
                return False

            registrar_evento(
                sesion["usuario"], "modificar", "exitoso",
                producto=identificador,
                anterior=anterior,
                nueva=cantidad
            )

            print("Cantidad actualizada.")
            return True

    print("Producto no encontrado:", identificador)
    return False


def main():
    print("Inventario académico — COMP2700")
    print("Estudiante:", input("Escriba su nombre: "))
    sesion = None

    while True:
        if sesion is None:
            nombre = input("Usuario (o salir): ")
            if nombre == "salir":
                break

            clave = input("Contraseña de prueba: ")
            sesion = autenticar(nombre, clave)
            continue

        print("1. Consultar | 2. Modificar | 3. Cerrar sesión | 0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            consultar_inventario(sesion)

        elif opcion == "2":
            identificador = input("ID del producto: ")
            entrada = input("Nueva cantidad: ")
            modificar_cantidad(sesion, identificador, entrada)

        elif opcion == "3":
            sesion = None
            print("Sesión cerrada.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
