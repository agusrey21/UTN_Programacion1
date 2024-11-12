#ejercicio1
def veces_q_repite(letra:str, cadena:str):
    contador = 0
    for i in cadena:
        if letra == i:
            contador += 1
    return contador

cadena = input("Ingrese una cadena de texto: ")
letra = input("Ingrese la letra que desea contar en la cadena: ")

resultado = veces_q_repite(letra, cadena)
print(f"Hay: {resultado} letras: {letra}")

#ejercicio2
def indices(indice1:str ,indice2:str , cadena:str):
    cadenax = ""
    for i in cadena:
        if i > indice1 and i < indice2:
            cadenax += i
    return cadenax

indice1 = "a"
indice2 = " "
cadena = "hola comoestas "
resultado(indice1,indice2,cadena)
print(resultado)