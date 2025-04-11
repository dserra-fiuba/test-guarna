def es_par(num):
    return num%2 == 0

def solicitar_numero():
    num = int(input("Ingrese numero positivo para conocer su paridad: "))
    while(num<0):
        print("Numero Invalido.")
        num = int(input("Ingrese numero positivo para conocer su paridad: "))
    return num

def main():
    numero = solicitar_numero()
    
    if (es_par(numero)):
        print("El numero es par")
    else:
        print("El numero no par")

main()
