def numeros_con_rango(rango):
    lista = []
    for i in range(10):
        numero = int(input("Ingrese un numero dentro del rango: "))
        while numero not in rango:
            numero = int(input("Por favor, Ingrese un numero dentro del rango: "))
        lista.append(numero)
    
    return lista

minimo = int(input("Ingrese un numero minimo para el rango deseado: "))
maximo = int(input("Ingrese un numero maximo para el rango deseado: "))
while maximo < minimo:
    maximo = int(input("Ingrese un numero maximo para el rango deseado QUE SEA MAYOR AL MINIMO: "))

rango = list(range(minimo, maximo+1))

resultado = numeros_con_rango(rango)
print(resultado)