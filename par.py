def es_par(num):
    return num%2 == 0

def main():
    numero = int(input("Ingrese numero positivo para conocer su paridad: "))
    if (es_par(numero)):
        print("El numero es par")
    else:
        print("El numero no par")

main()