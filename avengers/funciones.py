def swap(lista, i, j):
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux

def ordenar(lista, atributo, orden):
    
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if orden == 1 and lista[j][atributo] < lista[i][atributo]:
                swap(lista, i, j)
            elif orden == -1 and lista[j][atributo] > lista[i][atributo]:
                swap(lista, i, j)

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

def printear(atributo):
    print(f"""
          |---------------------------|
          | {"Nombre:".ljust(10)} {atributo["nombre"].ljust(14)} |
          | {"Identidad:".ljust(10)} {atributo["identidad"].ljust(14)} |
          | {"Altura:".ljust(10)} {atributo["altura"].ljust(14)} |
          | {"Peso:".ljust(10)} {atributo["peso"].ljust(14)} |
          | {"Fuerza:".ljust(10)} {atributo["fuerza"].ljust(14)} |
          | {"Inteligencia".ljust(10)} {atributo["inteligencia"].ljust(14)} |
          |---------------------------|
          """)

def print_todos(lista):
    for i in lista:
        printear(i)
        
def filtrar(lista, atributo, filtro):
    retorno = []
    for i in lista:
        if i[atributo] == filtro:
            retorno.append(i)
    
    return retorno

def promediar(lista, atributo, acumulador=0):
    
    if isnumero(lista[0][atributo]):
        if len(lista) > 0:
            for i in lista:
                acumulador += float(i[atributo])
            prom = acumulador/len(lista)
    else:
        print("La lista no contiene numeros en ese atributo.")
        prom = None
    
    return prom

def calcular_imc(peso, altura):
    
    imc = peso / (altura ** 2)
    return imc

def convertir_cm_a_m(distancia):
    retorno = distancia * 100
    return retorno

def obtener_datos(lista, atributo):
    datos = []
    for i in lista:
        bandera = False
        for j in datos:
            if i[atributo] == j:
                bandera = True
        if bandera == False:
            datos.append(i[atributo])
    return datos