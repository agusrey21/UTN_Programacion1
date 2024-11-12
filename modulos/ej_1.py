def get_int(mensaje:str, mensaje_error: str, minimo: int, reitentos: int) -> int|None:
    
        print(mensaje)
        
        for i in range(reitentos):
            numero = int(input("Ingrese un numero mayor a " + str(minimo) + " : "))
            if numero <= minimo:
                print(mensaje_error)
            else: 
                return numero
            

mensaje = input("Ingrese el texto inicial antes de pedir el numero: ")
mensaje_error = input("Cual seria el mensaje de error? ")
min = int(input("Ingrese el minimo a tener en cuenta para el numero pedido: "))
rei = int(input("Cuantos reintentos tiene?: "))

resultado = get_int(mensaje, mensaje_error, min, rei)

if resultado == None:
    print("Se supero la cantidad de intentos.")
else:
    print(f"El numero ingresado es: {resultado}")
            

def get_string(longitud: int, intentos: int, error: str) -> str|None:
    for i in range(intentos):
        cadena = input("Ingrese una cadena, teniendo en cuenta la longitud esperada de: "+ str(longitud) +": ")
        if len(cadena) > longitud:
            print(error)
            print(f"Se escribio una cadena de: "+ {len(cadena)})
        else: 
            return cadena
    
    return None

#ejercicio1
mensaje = input("Ingrese el texto inicial antes de pedir el numero: ")
mensaje_error = input("Cual seria el mensaje de error? ")
min = int(input("Ingrese el minimo a tener en cuenta para el numero pedido: "))
rei = int(input("Cuantos reintentos tiene?: "))

resultado = get_int(mensaje, mensaje_error, min, rei)

if resultado == None:
    print("Se supero la cantidad de intentos.")
else:
    print(f"El numero ingresado es: {resultado}")


#ejercicio2
long = int(input("Ingrese la longitud de la cadena: "))
inte = int(input("Intentos permitidos: "))
error = input("Ingrese el mensaje de error: ")

cade = get_string(long, inte, error)

if cade == None:
    print("Intentos terminados.")
else: 
    print(f"La cadena cumple con la longitud esperada de {long}")


            