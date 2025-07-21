import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

import psycopg2

def connect_db():
    try:
        connect = psycopg2.connect(
            database= DB_NAME,
            user= DB_USER,
            password= DB_PASSWORD,
            host= DB_HOST,
            port= DB_PORT
        )
        return connect
    except psycopg2.Error as error:
        print("Error conectando a la base de datos:", error)
        return None
    
def crear_tabla_profesor(connect):
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profesor (
            RUT INTEGER PRIMARY KEY,
            nombres VARCHAR(100),
            apellido_materno VARCHAR(100),
            apellido_paterno VARCHAR(100),
            direccion VARCHAR(200),
            ciudad VARCHAR(100)
        );
    """)
    connect.commit()
    cursor.close()
    print("\nTabla 'profesor' creada correctamente\n.")
   


def crear_profesor(connect,rut, nombres, apellido_paterno, apellido_materno, direccion, ciudad):
    cursor = connect.cursor()
    cursor.execute('INSERT INTO profesor (RUT, nombres, apellido_paterno, apellido_materno, direccion, ciudad) VALUES (%s, %s, %s, %s, %s, %s)',
                    (rut, nombres, apellido_paterno, apellido_materno, direccion, ciudad))
    connect.commit()
    cursor.close()
    print("\nProfesor creado exitosamente\n")

def leer_profesores(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM profesor;")
    lista_profesores = cursor.fetchall()
    cursor.close()
    return lista_profesores

def rut_exists(connect, rut):
    cursor = connect.cursor()
    cursor.execute("SELECT 1 FROM profesor WHERE RUT = %s", (rut,))
    exists = cursor.fetchone()is not None
    cursor.close()
    return exists

def actualizar_profesor(connect, rut, nombres, apellido_materno, apellido_paterno, direccion, ciudad):
    cursor = connect.cursor()
    cursor.execute("""
        UPDATE profesor
        SET nombres = %s,
            apellido_materno = %s,
            apellido_paterno = %s,
            direccion = %s,
            ciudad = %s
        WHERE RUT = %s
    """, (nombres, apellido_materno, apellido_paterno, direccion, ciudad, rut))
    connect.commit()
    cursor.close()
    print("\nDatos del profesor actualizados exitosamente.\n")


def eliminar_profesor(connect,rut):
    cursor = connect.cursor()
    cursor.execute("DELETE FROM profesor WHERE RUT= %s", (rut,))
    connect.commit()
    cursor.close()
    print("\nProfesor eliminado exitosamente\n")