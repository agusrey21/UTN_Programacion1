def get_string(longitud: int, intentos: int, error: str) -> str|None:
    for i in range(intentos):
        cadena = input("Ingrese una cadena, teniendo en cuenta la longitud esperada de: "+ str(longitud) +": ")
        if len(cadena) > longitud:
            print(error)
            print(f"Se escribio una cadena de: "+ {len(cadena)})
        else: 
            return cadena
    
    return None

long = int(input("Ingrese la longitud de la cadena: "))
inte = int(input("Intentos permitidos: "))
error = input("Ingrese el mensaje de error: ")

cade = get_string(long, inte, error)

if cade == None:
    print("Intentos terminados.")
else: 
    print(f"La cadena cumple con la longitud esperada de {long}")
            
