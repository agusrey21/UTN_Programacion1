def esta_en_lista(numero, lista):
    if numero in lista:
        return True
    else:
        return False
    
lista_num = [2,7,9,11,15,8,89,54,33,32,21,29,38]

num = int(input("Ingrese un numero: "))

resultado = esta_en_lista(num, lista_num)
if resultado:
    print("El numero se encuentra dentro de la lista.")
else:
    print("El numero no se encuentra en la lista.")