def es_par(num):
    return num%2 == 0

def solicitar_numero():
    numero = int(input("Ingrese numero positivo para conocer su paridad: "))
    while(numero<0):
        print("Numero Invalido.")
        numero = int(input("Ingrese numero positivo para conocer su paridad: "))
    return numero

def main():
    numero = solicitar_numero()
    
    if (es_par(numero)):
        print("El numero es par")
    else:
        print("El numero no par")

main()