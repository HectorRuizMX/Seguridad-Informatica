def suma():
    a = int(input("Ingresa el primer numero: "))
    b = int(input("Ingresa el segundo numero: "))
    
    suma = a + b
    binario = format(suma,"b")
    return print(f"Tu suma en número binario es {binario}")

def convert():
    numero = int(input("Ingresa un numero para convertir en binario: "))
    binario = format(numero,"b")
    return(f"Tu número en binario es: {binario}")