#FUNCIONES
#Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
#como parámetro.
def mostrar_numero(num:int)->int:
    print(num)

num = int(input("ingrese un numero: "))
mostrar_numero(num)
print()

#Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.
def pedir_numero()->int:
    num = int(input("Ingrese un numero: "))
    return num
pedir_numero()
print(f"El numero ingresado es: {num}")
print()

#Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
#función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
#programa principal realizando la invocación o llamada.
def es_par(num:int)->bool:
    if num % 2 == 0:
        return True
    else:
        return False
    
Numero = int(input("Ingrese un numero: "))

if es_par(Numero):
    print("es par")
else:
    print("no es par")
print()

#Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
#función Restar en sus 4 combinaciones.
# Restar1(int, int)->int:
# Restar2()->int:
# Restar3(int, int):
# Restar4():
def Restar1(a, b):
  return a - b

def Restar2():
  num1 = 10
  num2 = 5
  return num1 - num2

def Restar3(a, b):
  global resultado
  resultado = a - b

def Restar4():
  num1 = 20
  num2 = 12
  print(num1 - num2)


resultado_1 = Restar1(15, 7)
print(resultado_1)

resultado_2 = Restar2()
print(resultado_2)

Restar3(25, 10)
print(resultado) 

Restar4()

print()

