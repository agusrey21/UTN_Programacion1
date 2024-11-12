#10.Ingresar un número. Determinar si el número es primo o no.
num = int(input("Ingrese un numero: "))
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print(f"{num} es un numero primo")
else:
    print(f"{num} no es un numero primo")
    
