import random

def leer_entero(mensaje):
    """Solicita un número entero y repite la pregunta si la entrada no es válida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Escriba un número entero.")

def main():
    print("GENERADOR DE VALOR ALEATORIO")
    minimo = leer_entero("Ingrese el primer número (límite inferior): ")
    maximo = leer_entero("Ingrese el segundo número (límite superior): ")

    while minimo > maximo:
        print("El límite inferior no puede ser mayor que el superior.")
        minimo = leer_entero("Ingrese nuevamente el límite inferior: ")
        maximo = leer_entero("Ingrese nuevamente el límite superior: ")

    resultado = random.randint(minimo, maximo)
    print(f"El valor aleatorio generado entre {minimo} y {maximo} es: {resultado}")

if __name__ == "__main__":
    main()