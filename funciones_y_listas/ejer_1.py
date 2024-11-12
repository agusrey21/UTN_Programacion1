def pedir_nombres(lista, nombre):
    
    for i in range(10):
        nombre = input("Ingrese su nombre: ")
        lista.append(nombre)
    
    return lista

lista_nombres = []
nombres = ""

resultado = pedir_nombres(lista_nombres, nombres)
print(resultado)