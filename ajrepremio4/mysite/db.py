"""Archivo de conexión a la base de datos.
Se recomienda configurar las variables de entorno DB_HOST, DB_USER, DB_PASSWORD y DB_NAME
en PythonAnywhere (Web -> Environment variables) en lugar de dejar credenciales hardcodeadas.
"""
import os
import pymysql

# Valores por defecto pensados para despliegue en PythonAnywhere; sobreescribir mediante env vars
HOST = os.environ.get('DB_HOST', 'ajrepremio4.mysql.pythonanywhere-services.com')
USER = os.environ.get('DB_USER', 'ajrepremio4')
PASSWORD = os.environ.get('DB_PASSWORD', 'unpassword1')
DB = os.environ.get('DB_NAME', 'ajrepremio4$quiz_bd')

def obtener_conexion(con_dict=False):
    """Retorna una conexión PyMySQL; si con_dict=True usa cursores tipo diccionario"""
    if con_dict:
        clasecursor = pymysql.cursors.DictCursor
    else:
        clasecursor = pymysql.cursors.Cursor
    return pymysql.connect(host=HOST,
                           user=USER,
                           password=PASSWORD,
                           db=DB,
                           cursorclass=clasecursor)

# Alias
obtener_conexion_db = obtener_conexion
