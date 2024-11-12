from ejer_funciones import *
from ejer_funciones2 import *
print(" --------------------------------------------------------------------------------------- ")
print("                         MENU DE OPCIONES:")
print("""
      Para arrancar se deben importar las listas primero.
      1-Importar listas
      2-Datos de los usuarios de Mexico
      3-Nombre, mail y telefono de los usuarios de Brasil
      4-Datos del/los usuario/s mas joven/es
      5-Promedio de edad de los usuarios
      6-De los usuarios de Brasil, datos del usuario de mayor edad
      7-Datos de los usuarios de Mexico y Brasil cuyo codigo postal sea mayor a 8000
      8-Nombre, mail y telefono de los usuarios italianos mayores a 40 años.
      9-Datos de los usuarios de Mexico ordenados por nombre
      10-Datos del/los usuario/s mas joven/es ordenados por edad de manera ascendente
      11-Datos de los usuarios de Mexico y Brasil cuyo codigo postal sea mayor a 8000 ordenado por nombre y edad de manera ascendente
      
      """)

opcion = int(input("Importe las listas presionando la primera opcion: "))

while opcion != 1:
    opcion = int(input("Importe las listas presionando la primera opcion: "))

importar_listas()

while True:    
    opcion = int(input("Ingrese que opcion desea realizar: "))
    
    match opcion:
        case 2:
            lista_usuarios_mexico()
        case 3:
            lista_usuarios_brasil()
        case 4:
            usuario_mas_joven()
        case 5:
            promedio_edad()
        case 6:
            usuario_mayor_brasil()
        case 7:
            lista_usuario_mexico_brasil()
        case 8:
            lista_usuario_italiano()
        case 9:
            lista_mexico_ordenado()
        case 10:
            jovenes_ordenados()
        case 11:
            orden_usuario_mexico_brasil()
        case 12:
            print("Saliendo del programa")
            break
        case _:
            print("Opcion no valida, ingresa una correcta.")
        

