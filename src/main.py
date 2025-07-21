from BDD import connect_db, crear_tabla_profesor
from iu import main_iu

def main():
    connect = connect_db()
    if connect is None:
        print("\nNo se pudo conectar a la base de datos.")
        return
    
    crear_tabla_profesor(connect)

    try:
        main_iu(connect)
    finally:
        connect.close()

if __name__ == "__main__":
    main()
