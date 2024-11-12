def sumar_naturales(numero: int)->int:
    if numero <= 0:
        return 0
    else:
        return numero + sumar_naturales(numero - 1)

num = int(input("Ingrese un numero mayor a 0: "))
while num <= 0:
    num = int(input("Ingrese un numero mayor a 0: "))
    
resultado = sumar_naturales(num)
print(f"el resultado de los numeros primos desde 1 a {num} es de: {resultado}")
