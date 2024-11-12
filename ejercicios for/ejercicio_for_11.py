#11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
#número ingresado. Informar cuántos números primos se encontraron
numero = int(input("Ingrese un número: "))
contador = 0
print(f"Los números primos entre 1 y {numero} son:")
for num in range(2, numero + 1):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
        contador += 1
print("Se encontraron", contador, "números primos.")