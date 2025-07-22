from BDD import connect_db, crear_tabla_profesor, crear_tablas_consulta
from iu import main_iu

def main():
    connect = connect_db()
    if connect is None:
        print("\nNo se pudo conectar a la base de datos.")
        return
    
    crear_tabla_profesor(connect)
    crear_tablas_consulta(connect)

    try:
        main_iu(connect)
    finally:
        connect.close()

if __name__ == "__main__":
    main()
