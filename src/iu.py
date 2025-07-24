from BDD import crear_profesor, ejecutar_consulta, leer_profesores, rut_exists, actualizar_profesor, eliminar_profesor
from validaciones import string, num, stringNum
def menu():
    print("------------------------------------")
    print("-------- Mini aplicacion --------")
    print("------------------------------------")
    print("1. Crear Profesor")
    print("2. Leer Profesores")
    print("3. Actualizar Profesor")
    print("4. Eliminar Profesor")
    print("5. Ejecutar Consulta")
    print("0. Salir")
    print("------------------------------------")
    print("------------------------------------")
    return input("Seleccione una opcion: ")

def obtener_datos_profe():
    rut = num("Ingrese rut: ")
    nombres = string("Ingrese Nombres: ")
    apellido_materno = string("Ingrese apellido paterno: ")
    apellido_paterno = string("Ingrese apellido materno: ")
    direccion = stringNum("Ingrese direccion: ")
    ciudad = string("Ingrese ciudad: ")
    print("\n")
    return (rut, nombres, apellido_materno, apellido_paterno, direccion, ciudad)

def actualizar_datos_profe():
    nombres = string("Ingrese Nombres: ")
    apellido_materno = string("Ingrese apellido paterno: ")
    apellido_paterno = string("Ingrese apellido materno: ")
    direccion = stringNum("Ingrese direccion: ")
    ciudad = string("Ingrese ciudad: ")
    print("\n")
    return (nombres, apellido_materno, apellido_paterno, direccion, ciudad)
    
print("\n")

def obtener_rut():
    return num("Ingrese rut del profesor: ")

def mostrar_profes(profesores):
    print("\nPROFESORES:")
    for profesor in profesores:
        print(profesor)
        print("\n")


def main_iu(connect):
    while True:
        opcion = menu()

        if opcion == '1':
            while True:
                rut = obtener_rut()
                if not rut_exists(connect, rut):
                    print("\n--------------------------------------------------------------------------")
                    print("Rut No encontrado en la base de datos. Continue la insercion de datos:")
                    print("----------------------------------------------------------------------------\n")
                    datos = obtener_datos_profe()
                    crear_profesor(connect, *datos)
                    break
                else:
                    print("\nEl RUT ingresado ya existe. Intente con otro.\n")
        elif opcion == '2':
            profesores = leer_profesores(connect)
            if not profesores:
                print("\nNo existen profesores en la base de datos.\n")
            else:
                mostrar_profes(profesores)
        elif opcion == '3':
            while True:
                rut = obtener_rut()
                if rut_exists(connect, rut):
                    print("\n---------------------------------------------")
                    print("Profesor encontrado. Actualice los datos:")
                    print("---------------------------------------------\n")
                    print("\n---------------------------------------------")
                    print("Ingrese los nuevos datos del profesor: ")
                    print("---------------------------------------------\n")
                    nuevos_datos = actualizar_datos_profe()
                    actualizar_profesor(connect, rut, *nuevos_datos)
                    break
                else: 
                    print("\nEl RUT ingresado no existe en la base de datos. Intente nuevamente.\n")
        elif opcion == '4':
            while True:
                rut = obtener_rut()
                if rut_exists(connect, rut):
                    eliminar_profesor(connect, rut)
                    break
                else:
                    print("\nEl RUT ingresado no existe en la base de datos. Intente nuevamente.\n")
        elif opcion == '5':
            ejecutar_consulta(connect)
        elif opcion == '0':
            print("Saliendo de la aplicación.")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.\n")
