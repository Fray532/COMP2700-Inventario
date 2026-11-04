import json
from pathlib import Path
from seguridad import crear_hash

RAIZ = Path(__file__).resolve().parent
USUARIOS = RAIZ / "usuarios.json"


def migrar_usuarios():
    usuarios = json.loads(USUARIOS.read_text(encoding="utf-8"))

    for usuario in usuarios:
        if "clave" in usuario:
            usuario["hash"] = crear_hash(usuario["clave"])
            del usuario["clave"]

    USUARIOS.write_text(
        json.dumps(usuarios, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print("Contraseñas convertidas a hashes. Campo clave eliminado.")


if __name__ == "__main__":
    migrar_usuarios()