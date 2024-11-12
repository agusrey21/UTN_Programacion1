def numero_a_guardar(posicion, numero):
    
    lista = [0]*10
    lista[posicion] = numero
    
    return lista

posicion_deseada = int(input("Ingrese en que posicion desea poner el numero: (entre 0 y 9) "))
while posicion_deseada < 0 or posicion_deseada > 9:
    posicion_deseada = int(input("Ingrese en que posicion desea poner el numero: (entre 0 y 9) "))

num = int(input("Que numero desea ingresar?: "))

resultado = numero_a_guardar(posicion_deseada, num)
print(resultado)