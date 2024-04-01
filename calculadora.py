def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2 

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        resultado = num1/num2
    else:
        print("La operación es inválida")

    return resultado

operacion = int(input("""Selecciones la operación que desea realizar:
                      1) Suma
                      2) Resta
                      3) Multiplicación
                      4) División
                      """))

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if operacion == 1:
    resultado = sumar(num1, num2)
elif operacion == 2:
    resultado = restar(num1, num2)
elif operacion == 3:
    resultado = multiplicar(num1, num2)
elif operacion == 4:
    resultado = dividir(num1, num2)
else:
    print("Operación inválida")

print("El resultado de la operación es: ", resultado) 