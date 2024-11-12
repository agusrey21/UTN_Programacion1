#Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
#los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
#variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
#la operación de dichos valores a través de una función. Mostrar el resultado por
#pantalla.
def sumar(num1:int, num2:int)->int:
    resultado = num1 + num2
    return resultado

def restar(num1:int,num2:int)->int:
    resultado2 = num1 - num2
    return resultado2

numero1 = int(input("Ingrese un primer numero: (entre 10 y 100) "))
while numero1 < 10 or numero1 > 100:
    numero1 = int(input("Ingrese un primer numero: (entre 10 y 100) "))
    
numero2 = int(input("Ingrese un segundo numero: (entre 10 y 100) "))
while numero2 < 10 or numero2 > 100:
    numero2 = int(input("Ingrese un segundo numero: (entre 10 y 100) "))
    
operacion = input("Ingrese que operacion desea hacer: ('s' -sumar, 'r' -restar) ").lower()
while operacion != "s" and operacion != "r":
    operacion = input("Ingrese que operacion desea hacer: ('s' -sumar, 'r' -restar) ").lower()

if operacion == "s":
    suma = sumar(numero1,numero2)
    print(f"La suma entre {numero1} y {numero2} es: {suma}")
else:
    resta = restar(numero1,numero2)
    print(f"La resta entre {numero1} y {numero2} es: {resta}")

