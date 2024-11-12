#Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La 
#función deberá seguir el siguiente prototipo:
#Definición:
#La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de 
#los dos anteriores:
def get_int(mensaje:str, mensaje_error: str, minimo: int, reitentos: int) -> int|None:
    
        print(mensaje)
        
        for i in range(reitentos):
            numero = int(input("Ingrese un numero mayor a " + str(minimo) + " : "))
            if numero <= minimo:
                print(mensaje_error)
            else: 
                return numero
            
            
def calcular_fibonacci(numero: int)-> int:
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
    
num = get_int("Ingrese un numero", "ALERTA", 5, 6)
resultado = calcular_fibonacci(num)
print(resultado)