def pedir_numero()->int:
    num = int(input("Ingrese un numero: "))
    return num

def es_par(num:int)->bool:
    if num % 2 == 0:
        return True
    else:
        return False

def sumar(num1:int, num2:int)->int:
    resultado = num1 + num2
    return resultado

def restar(num1:int,num2:int)->int:
    resultado2 = num1 - num2
    return resultado2

def mostrar_numero()->int:
    min = int(input("Ingrese un numero minimo: "))
    max = int(input("Ingrese un numero maximo: "))
    while min > max:
        max = int(input("Ingrese un numero maximo:(mayor al minimo) "))
    
    return min, max

def swapper(lista:list, i:int, j:int):
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux