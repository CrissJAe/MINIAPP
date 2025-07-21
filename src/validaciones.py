def string(prompt):
    while True:
        entrada = input(prompt).strip()
        if entrada and entrada.replace(" ", "").isalpha():  # Solo permite letras y espacios
            return entrada
        else:
            print("Entrada inválida. Intente nuevamente.")


def num(prompt):
    while True:
        try:
            numero = int(input(prompt))
            return numero
        except ValueError:
            print("Entrada inválida. intente nuevamente.")

def stringNum(prompt):
    while True:
        entrada = input(prompt).strip()
        if entrada and all(c.isalnum() or c.isspace() for c in entrada):  # A diferencia de la función string, permite también números
            return entrada
        else:
            print("Entrada inválida. Intente nuevamente.")