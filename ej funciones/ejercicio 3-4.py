#Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
#un rango determinado pasado por parámetro “desde”-“hasta”.
def pedir_numero(desde:int,hasta:int)->int:
    numero = int(input(f"Ingrese un numero entre el rango:[{desde}/{hasta}] "))
    while numero < desde or numero > hasta:
        numero = int(input(f"Ingrese un numero entre el rango:[{desde}/{hasta}] "))
        
    return numero

minimo = int(input("Ingrese un numero minimo: "))
maximo = int(input("Ingrese un numero maximo: "))
while minimo > maximo:
    maximo = int(input("Ingrese un numero maximo:(mayor al minimo) "))

resultado = pedir_numero(minimo, maximo)
print(f"el numero ingresado entre {minimo}/{maximo} fue: {resultado}")
print()

def mostrar_numero()->int:
    min = int(input("Ingrese un numero minimo: "))
    max = int(input("Ingrese un numero maximo: "))
    while min > max:
        max = int(input("Ingrese un numero maximo:(mayor al minimo) "))
    
    return min, max

min_r, max_r= mostrar_numero()
print(f"El minimo es {min_r} y el maximo es {max_r}")

num = int(input("Ingrese un numero entre el maximo y minimo antes mostrado: "))
while num < min_r or num > max_r:
    print(f"El minimo es {min_r} y el maximo es {max_r}")
    num = int(input("Ingrese un numero entre el maximo y minimo antes mostrado: "))
    
print(f"el numero ingresado entre {min_r}/{max_r} fue: {num}")


