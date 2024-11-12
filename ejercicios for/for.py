#1. Mostrar los números ascendentes desde el 1 al 10
for i in range(0,11):
    print(i)
print(" ")

#2. Mostrar los números descendentes desde el 10 al 1
for i in range(10, 0, -1):
    print(i)
print(" ")

#3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
num = int(input("Ingrese un numero: "))
for i in range(0, num + 1):
    print(i)
print(" ")

#4. Ingresar un número y mostrar la tabla de multiplicar de ese número.
num = int(input("Ingrese un numero: "))
for i in range(0, 10 + 1):
    print(f"{num} x {i} : {num * i}")
print(" ")

#5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
#número 0. Mostrar la suma y el promedio de todos los números.
suma = 0
contador = 0
prom = 0
for i in range(10):
    num = int(input("Ingrese un numero: "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    prom = suma / contador
print(f"la suma es: {suma}")
print(f"el promedio es de: {prom}")
print(" ")

#6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
for i in range (1, 11):
    if i % 3 == 0:
        print(i)
print(" ")

#7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
for i in range (2, 51, 2):
    print(i)
print(" ")

#8. Realizar un programa que permita mostrar una pirámide de números.
altura = int(input("Ingrese la altura de la pirámide: "))
for i in range(1, altura + 1):
    print(' ' * (altura - i), end='')
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print(" ")

#9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
#el número ingresado. Mostrar la cantidad de divisores encontrados.
num = int(input("Ingrese un numero: "))
cont = 0
print(f"Los divisores de {num} son: ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        cont += 1
print(f"La cantidad de divisores fue de: {cont}")
print(" ")





    