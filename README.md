**Inventario académico — COMP2700**

Estudiante: Frazier Gomez Guzman

**Descripción**

Este proyecto es una aplicación de inventario en Python que se utiliza desde la terminal. Trabajé con la base suministrada por el profesor, base_estudiante.zip, para corregir sus problemas de seguridad. Los datos y las cuentas son ficticios.

Admin puede consultar el inventario y modificar cantidades. User solamente puede consultar. Las cantidades deben ser números enteros entre 0 y 1000, incluyendo ambos límites.

**Requisitos**

- Python 3.10 o posterior.
- argon2-cffi, indicado en requirements.txt.

**Instalación y ejecución en Windows CMD**

Abra una terminal dentro de la carpeta donde está app.py y ejecute estos comandos uno a la vez:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python app.py
```

Cuando el programa lo solicite, escriba su nombre e ingrese con una de las cuentas de prueba.

**Cuentas ficticias de prueba**

- Usuario: admin | Contraseña: AdminDemo2700!
- Usuario: user | Contraseña: UserDemo2700!

Estas cuentas son públicas y solamente se utilizan para el ejercicio. En usuarios.json, las contraseñas están guardadas como hashes Argon2id con salt y se eliminó el campo clave.

**Archivos del proyecto**
- app.py
- seguridad.py
- usuarios.json
- inventario.json
- auditoria.jsonl
- requirements.txt
- migrar_usuarios.py
- prueba_permisos.py
- prueba_cantidades.py
- prueba_inventario.py


**Pruebas**

Para ejecutar los scripts de prueba:

```bat
python prueba_permisos.py
python prueba_cantidades.py
python prueba_inventario.py
```

Para repetir las pruebas, comence con P001 en 10 y ejecute los scripts en el orden indicado. La prueba de permisos verifica que user no pueda modificar cantidades y que tampoco se pueda modificar sin iniciar sesión.

La prueba de cantidades utiliza -1, 1001, abc, 2.5 y una entrada vacía para comprobar que se rechacen. También prueba 0 y 1000, que deben aceptarse. Al terminar, devuelve P001 a 10.

La prueba de inventario verifica que admin y user puedan consultar. Después, como admin, cambia P001 de 10 a 20 e intenta modificar P999. P001 queda en 20 al finalizar.

También probé entrar con datos correctos e incorrectos y cerrar el programa para verificar que los cambios se guardaran. Para probar el archivo ausente y el JSON inválido, hice un respaldo y restauré el archivo al terminar.

**Auditoría**

El archivo auditoria.jsonl guarda un evento JSON por línea con la fecha, hora, usuario, acción y resultado.

Cuando se cambia una cantidad, también se guarda el producto y la cantidad anterior y nueva. Se registran los accesos correctos, los fallidos y los intentos de modificar sin permiso. No se guardan contraseñas ni hashes.

**Uso de IA**

Utilicé ChatGPT para entender los requisitos y las partes del programa que se me hacían difíciles. También recibí ayuda para corregir código y preparar los scripts de prueba.

Apliqué los cambios y ejecuté las pruebas en mi computadora para comprobar que los resultados fueran los esperados.

**Fuentes del proyecto**

- Base educativa base_estudiante.zip e instrucciones del proyecto.
- Archivo seguridad.py.
- ChatGPT, utilizado como apoyo para las explicaciones, correcciones y pruebas.

**Referencias adicionales para consulta**

- Coders Arcade. Python JSON Tutorial Made Easy: Full Course. YouTube.  
  https://www.youtube.com/watch?v=AppKIaME5_I

- Working With JSON Data in Python.  
  Acsany, P. (2026, October 24). Working with JSON data in Python. Real Python. https://realpython.com/python-json/

- W3SChools Python Json 
  Python JSON. (n.d.). W3Schools. https://www.w3schools.com/python/python_json.asp

- What is Argon2
  What is Argon2? - argon2-cffi 25.1.0 documentation. (n.d.). https://argon2-cffi.readthedocs.io/en/stable/argon2.html#

**Limitaciones**

Los permisos funcionan dentro del programa. Una persona que pueda editar los archivos locales también podría cambiar los usuarios, el inventario o la auditoría.

La sesión se guarda como un diccionario. Si alguien puede ejecutar código dentro del mismo proceso, podría cambiar sus datos.

El proyecto no tiene MFA, cifrado del inventario ni protección contra cambios externos al log.

Si falla el registro de auditoría, aparece un mensaje de error, pero el cambio del inventario puede haberse guardado. Esto se podría mejorar haciendo que el cambio y su registro se guarden juntos.
