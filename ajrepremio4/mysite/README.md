# Despliegue en PythonAnywhere (guía rápida)

_Este proyecto es una aplicación Flask que usa MySQL (PyMySQL), envío de correo (Flask-Mail) y pandas para exportar resultados._

## Resumen de pasos (para principiantes)

1. Crea una cuenta en https://www.pythonanywhere.com/ y accede.
2. Sube tu código al servidor:
   - Recomiendo usar Git: crea un repo, sube el proyecto y en PythonAnywhere clona el repo en tu directorio home.
   - Alternativamente, en la pestaña "Files" puedes subir `mysite` manualmente.
3. Crea un virtualenv en PythonAnywhere (bash):

```bash
python3.10 -m venv ~/venv-mysite
source ~/venv-mysite/bin/activate
pip install -r ~/mysite/requirements.txt
```

4. Crea la base de datos MySQL desde la pestaña "Databases" en PythonAnywhere. Anota el nombre de usuario y la base de datos.

5. Ejecuta el esquema SQL (`schema.sql`) para crear las tablas (en Consoles -> Bash):

```bash
# Subir schema.sql al home o asegurarte de la ruta
mysql -u <tu_usuario> -p'<tu_contraseña>' <tu_usuario>$<nombre_bd> < ~/mysite/schema.sql
```

(En PythonAnywhere la base de datos suele llamarse `tu_usuario$nombre_bd`)

6. Configura variables de entorno (Web -> Environment variables):

- `DB_HOST` (ej: `yourusername.mysql.pythonanywhere-services.com`)
- `DB_USER` (tu usuario)
- `DB_PASSWORD` (la contraseña que configuraste)
- `DB_NAME` (ej: `tu_usuario$nombre_bd`)
- `MAIL_PASSWORD` (contraseña de aplicación si usas Gmail)
- Opcional: `MAIL_USERNAME`, `MAIL_SERVER`, `MAIL_PORT` si no quieres los valores por defecto

7. En la pestaña "Web" crea una nueva Web App:
   - Selecciona manual configuration -> Python 3.x
   - En "Source code" apunta a la carpeta `~/mysite`
   - En "Virtualenv" apunta a `~/venv-mysite`
   - Edita el WSGI file (haz click en el link) y asegúrate de que cargue tu app:

```python
# dentro del WSGI file (al final)
import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

8. Reload la web app desde la pestaña "Web" y revisa los logs si hay errores (`error.log`, `server.log`).

## Notas de seguridad
- No dejes contraseñas en el código. Usa las Environment variables de PythonAnywhere.
- Para Gmail genera una contraseña de aplicación y usa `MAIL_PASSWORD` con esa cadena.

## Comprobaciones rápidas
- En una consola bash en PythonAnywhere, activa el virtualenv y ejecuta `python -m pip list` para confirmar que las dependencias están instaladas.
- Revisa `~/mysite/error.log` para errores de import o de bases de datos.

---

Si quieres, puedo:
- Generar un `requirements.txt` más completo con versiones fijas.
- Ayudarte a preparar el WSGI exacto y las variables de entorno con los valores reales.
- Conectarme (paso a paso) mientras ejecutas la configuración en PythonAnywhere.