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
    
def ordenar(lista, atributo, orden):
    
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if orden == 1 and lista[j][atributo] < lista[i][atributo]:
                swapper(lista, i, j)
            elif orden == -1 and lista[j][atributo] > lista[i][atributo]:
                swapper(lista, i, j)

def obtener_min_max(lista, atributo, opcion):
    
    num = (lista[0][atributo])
    lista_filtrada = [lista[0]]
    if isnumero(num):
        num = float(num)
        for i in range(len(lista)):
            if opcion == 1 and float(lista[i][atributo]) > num:
                num = float(lista[i][atributo])
                lista_filtrada = [lista[i]]
            elif opcion == -1 and float(lista[i][atributo]) < num:
                num = float(lista[i][atributo])
                lista_filtrada = lista[i]
            elif float(lista[i][atributo]) == num and i > 0:
                lista_filtrada.append(lista[i])
            elif opcion != 1 and opcion != -1:
                print("Opcion incorrecta")
    else:
        print("la lista no tiene numeros en esa posicion.")
        
    return lista_filtrada

def isnumero(numero):
    retorno = False
    if isfloat(numero): retorno = True
    if numero.isdigit(): retorno = True
    return retorno

def isfloat(cadena):
    retorno = True
    if cadena.count(".") == 1:
        for i in cadena:
            if not i.isdigit() and i != ".":
                retorno = False
    else:
        retorno = False
        
    return retorno

def print_todos(lista):
    for i in lista:
        print(i, end=" ")
        
def filtrar(lista, atributo, filtro):
    retorno = []
    for i in lista:
        if i[atributo] == filtro:
            retorno.append(i)
    
    return retorno