\# Inventario académico — COMP2700



Estudiante: Frazier Gomez Guzman



\## Descripción



Aplicación de inventario en Python para terminal, corregida a partir de

base\_estudiante.zip. Utiliza archivos JSON y cuentas exclusivamente ficticias.



Admin puede consultar y modificar cantidades. User solamente puede consultar.

Las cantidades deben ser números enteros entre 0 y 1000, inclusive.



\## Requisitos



\- Python 3.10 o posterior.

\- argon2-cffi, según requirements.txt.



\## Instalación y ejecución en Windows CMD



Abra una terminal dentro de la carpeta que contiene app.py.



Ejecute los siguientes comandos, uno a la vez:



```bat

python -m venv .venv

.venv\\Scripts\\activate.bat

python -m pip install -r requirements.txt

python app.py

```



Escriba su nombre cuando el programa lo solicite.



\## Cuentas ficticias de prueba



\- Usuario: admin | Contraseña: AdminDemo2700!

\- Usuario: user | Contraseña: UserDemo2700!



Estas credenciales son públicas y se utilizan únicamente para este ejercicio.

usuarios.json almacena hashes Argon2id con salt, sin el campo clave.



\## Archivos



\- app.py: autenticación, permisos, inventario y auditoría.

\- seguridad.py: funciones de protección de contraseñas suministradas.

\- usuarios.json: cuentas ficticias con hashes.

\- inventario.json: productos y cantidades.

\- auditoria.jsonl: eventos reales generados durante las pruebas.

\- requirements.txt: dependencia externa.

\- migrar\_usuarios.py: convierte las claves originales en hashes.

\- prueba\_permisos.py: prueba permisos mediante llamadas directas.

\- prueba\_cantidades.py: prueba entradas inválidas y límites válidos.

\- prueba\_inventario.py: prueba consultas y modificaciones.



El archivo final de usuarios ya está migrado. No es necesario ejecutar

migrar\_usuarios.py para utilizar la versión entregada.



\## Pruebas



```bat

python prueba\_permisos.py

python prueba\_cantidades.py

python prueba\_inventario.py

```



Para reproducir la secuencia original, comience con P001 en 10.

prueba\_permisos.py comprueba que los intentos rechazados no cambien el archivo.

prueba\_cantidades.py modifica P001 durante las pruebas y lo restaura a 10.

prueba\_inventario.py termina con P001 en 20.



También se probaron manualmente los inicios de sesión, la persistencia

después de reiniciar y los errores de inventario ausente o JSON inválido.

Para las pruebas de errores se utilizó un respaldo y se restauró el archivo.



\## Auditoría



Cada línea de auditoria.jsonl contiene un evento JSON con fecha/hora,

usuario, acción y resultado. Los cambios exitosos incluyen producto,

cantidad anterior y cantidad nueva. No se registran contraseñas ni hashes.



\## Uso de IA y fuentes



Utilicé ChatGPT de OpenAI para comprender los requisitos, proponer

correcciones y preparar scripts de prueba. Verifiqué las sugerencias

ejecutando el programa y comparando resultados esperados y obtenidos.

Por ejemplo, comprobé que user no pudiera modificar P001 mediante una

llamada directa y que el archivo permaneciera sin cambios.



La base del programa y seguridad.py fueron suministrados por el profesor.

Se utilizó argon2-cffi mediante las funciones de seguridad.py.



\## Limitaciones



Los permisos se aplican dentro del programa. Una persona con acceso de

escritura a los archivos locales puede alterar usuarios, inventario o log.

La sesión se representa mediante un diccionario dentro del proceso;

no protege contra alguien que pueda ejecutar código arbitrario allí.



El prototipo no incluye MFA, cifrado del inventario ni protección del log

contra modificaciones externas. Si falla la escritura del log, se muestra

un error, pero una modificación del inventario ya guardada no se revierte.

Una mejora sería coordinar el guardado del cambio y su registro de auditoría.

