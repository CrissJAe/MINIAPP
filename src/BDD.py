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
    print("\nTabla 'profesor' creada correctamente.\n")

def crear_tablas_consulta(connect):
    cursor = connect.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS curso (
            codigo INTEGER PRIMARY KEY,
            año INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumno (
            RUT INTEGER PRIMARY KEY,
            nombres VARCHAR(100),
            apellido_paterno VARCHAR(100),
            apellido_materno VARCHAR(100),
            fecha_nacimiento DATE,
            direccion VARCHAR(200),
            ciudad VARCHAR(100),
            codigo_curso INTEGER,
            FOREIGN KEY (codigo_curso) REFERENCES curso(codigo)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS apoderado (
            RUT INTEGER PRIMARY KEY,
            nombres VARCHAR(100),
            apellido_paterno VARCHAR(100),
            apellido_materno VARCHAR(100),
            direccion VARCHAR(200),
            ciudad VARCHAR(100)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS representa (
            rut_alumno INTEGER,
            rut_apoderado INTEGER,
            fecha_inicio DATE,
            fecha_termino DATE,
            PRIMARY KEY (rut_alumno, rut_apoderado),
            FOREIGN KEY (rut_alumno) REFERENCES alumno(RUT),
            FOREIGN KEY (rut_apoderado) REFERENCES apoderado(RUT)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS esjefe (
            codigo_curso INTEGER,
            rut_profesor_jefe INTEGER,
            PRIMARY KEY (codigo_curso, rut_profesor_jefe),
            FOREIGN KEY (codigo_curso) REFERENCES curso(codigo),
            FOREIGN KEY (rut_profesor_jefe) REFERENCES profesor(RUT)
        );
    """)

    connect.commit()
    cursor.close()
    print("\nTablas para consulta creadas correctamente.\n")
   


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

def insercion_datos(connect):
    cursor = connect.cursor()
    try:
        cursor.execute("""
            INSERT INTO profesor (RUT, nombres, apellido_paterno, apellido_materno, direccion, ciudad) VALUES
            (12435678, 'Florencia Luciana', 'Sanchez', 'Vergara', 'Av collao 5463', 'Concepcion'),
            (19224985, 'Sebastian', 'Espinoza', 'Gonzalez', 'Paicavi 4090', 'Concepcion'),
            (20432109, 'Ana Paola', 'Lopez', 'Martinez', 'Av Ohiggins 3009', 'Santiago');
        """)

        cursor.execute("""
            INSERT INTO curso (codigo, año) VALUES
            (101, 2024),
            (102, 2025),
            (103, 2025);
        """)
        
        cursor.execute("""
            INSERT INTO alumno (RUT, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, direccion, ciudad, codigo_curso) VALUES
            (21233897, 'Juan', 'Perez', 'Gomez', '2000-01-01', 'Av collao 123', 'Santiago', 101),
            (22189098, 'Ana', 'Lopez', 'Martinez', '2001-02-02', 'Av siempre viva 456', 'Concepcion', 102),
            (21890001, 'Martin Arnoldo', 'Elgueda', 'Pulido', '2005-04-13', 'Calle agustin 123', 'Concepcion', 103),
            (21681388, 'Cristopher Andres', 'Jimenez', 'Aedo', '2004-09-30', 'Los queules 870', 'Concepcion', 103);
        """)
        
        cursor.execute("""
            INSERT INTO apoderado (RUT, nombres, apellido_paterno, apellido_materno, direccion, ciudad) VALUES
            (15678654, 'Pedro', 'Martinez', 'Lopez', 'Av collao 123', 'Santiago'),
            (15897653, 'Laura', 'Sanchez', 'Perez', 'Av siempre viva 456', 'Concepcion'),
            (16789089, 'Maria', 'Garcia', 'Hernandez', 'Calle agustin 123', 'Concepcion'),          
            (13378765, 'Carlos', 'Ramirez', 'Fernandez', 'Los queules 870', 'Concepcion');     
        """)
        
        cursor.execute("""
            INSERT INTO representa (rut_alumno, rut_apoderado, fecha_inicio, fecha_termino) VALUES
            (21233897, 15678654, '2023-03-01', NULL),
            (22189098, 15897653, '2023-04-01', NULL),
            (21890001, 16789089, '2023-05-01', NULL),
            (21681388, 13378765, '2023-08-01', NULL);
        """)
        
        cursor.execute("""
            INSERT INTO esjefe (codigo_curso, rut_profesor_jefe) VALUES
            (101, 20432109),
            (102, 19224985),
            (103, 12435678);
        """)
        
        connect.commit()
        print("\nDatos insertados correctamente.\n")
    except Exception as error:
        print(f"\nError al insertar datos: {error}\n")
    finally:
        cursor.close()

def datos_existentes(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM alumno;")
    cantidad = cursor.fetchone()[0]
    cursor.close()
    return cantidad > 0    

def ejecutar_consulta(connect):
    cursor = connect.cursor()
    try:
        cursor.execute("""
            SELECT a.nombres, c.codigo, p.nombres, p.apellido_paterno, ap.nombres
            FROM alumno a
            JOIN representa r ON a.rut = r.rut_alumno
            JOIN apoderado ap ON r.rut_apoderado = ap.rut
            JOIN curso c ON a.codigo_curso = c.codigo
            JOIN esjefe ej ON c.codigo = ej.codigo_curso
            JOIN profesor p ON ej.rut_profesor_jefe = p.rut
            WHERE c.año = 2025;
        """)
        consulta = cursor.fetchall()
        print("\nResultado de la consulta:\n")
        for fila in consulta:
            print(fila)
            print("\n")
    except Exception as error:
        print(f"\nError al ejecutar la consulta: {error}\n")
    finally:
        cursor.close()
