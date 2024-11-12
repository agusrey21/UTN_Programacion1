from validate import validate_length, validate_number

def get_int() -> int|None:
    
    numero = input("Ingrese un numero entero mayor a 0: ")
    num = validate_number(numero, "int")
    
    return num
    
    
            
def get_string(longitud) -> str|None:
    
    cadena = input("Ingrese una cadena, teniendo en cuenta la longitud esperada de: "+ str(longitud) +": ")
    cadena = validate_length(cadena, longitud)
    
    return cadena

def get_float() -> float|None:
    
    num_flo = input("Ingrese un numero flotante positivo: ")
    flo = validate_number(num_flo, "float")
    
    return flo

entero = get_int()
if entero == None:
    print("No es un numero entero")
else: 
    print(f"{entero} es un numero entero.")
    
flotante = get_float()
if flotante == None:
    print("No es un numero flotante.")
else: 
    print(f"{flotante} es un numero flotante.")

string = get_string(20)
if string == None:
    print("No supera las palabras esperadas.")
else:
    print("supera las palabras esperadas.")
