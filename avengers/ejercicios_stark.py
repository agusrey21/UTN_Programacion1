from avengers.funciones import *
from avengers.data_stark import lista_personajes

from copy import deepcopy
from os import system

heroes = deepcopy(lista_personajes)

def menu():
    opcion = input('''
            1. Listar ordenado por Nombre.
            2. Listar Masculinos débiles.
            3. Cantidad por color de ojos.
            4. Listar por color de Pelo.
            5. Listar inteligencia.
            6. Listar Promedio.
            7. Asignar IMC.
            8. Salir
            Ingrese una opcion: ''')
            
    return opcion

def opcion_uno():

    ordenar(heroes, "nombre", 1)
    print_todos(heroes)

def opcion_dos():
    lista_filtrada = obtener_min_max(heroes, "fuerza", -1)
    ordenar(lista_filtrada, "fuerza", 1)
    print(f'''
        |-------------------------------------------------|
        |    {'Los personajes con menos fuerza son:'.center(44)} |
        |-------------------------------------------------|''')
    print_todos(lista_filtrada)

def opcion_tres():
    lista_color_ojos = obtener_datos(heroes,"color_ojos")
    for i in lista_color_ojos:
        cant = 0
        for j in heroes:
            cant = cant + 1 if j["color_ojos"] == i else cant
        print(f'''
        |--------------------------------------------------------------|
        
            Hay {cant} superheroes 
            con color de ojos {i}   ''')
    print(f'''
        |--------------------------------------------------------------|''')

def opcion_cuatro():
    lista_color_pelo = obtener_datos(heroes,"color_pelo")
    for e in lista_color_pelo:
        lista_filtrada = filtrar(heroes, "color_pelo", e)
        print(f"Color de pelo: {e}")
        print_todos(lista_filtrada)
        
def opcion_cinco():
    tipo_inteligencia = obtener_datos(heroes,"inteligencia")
    for e in tipo_inteligencia:
        lista_filtrada = filtrar(heroes, "inteligencia", e)
        print(f"Inteligencia: {e}")
        print_todos(lista_filtrada)

def opcion_seis():
    mujeres = filtrar(heroes, "genero", "F")
    prom = promediar(mujeres, "fuerza")
    for h in heroes:
        if int(h["fuerza"]) > prom:
            print(f'''
        |-------------------------------------------------|      
        |    {"Nombre:".ljust(14)} {h["nombre"].ljust(30)}|
        |    {"Peso:".ljust(14)} {str("%.2f" %float(h["peso"])).ljust(30)}|
        |-------------------------------------------------|''')

def opcion_siete():
    for h in heroes:
        imc = calcular_imc(float(h["peso"]),convertir_cm_a_m(float(h["altura"])))
        h["imc"] = imc
        printear(h)