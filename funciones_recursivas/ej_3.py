def sumar_digitos(numero: int)-> int:
    if numero == 0:
        return 0
    else:
        ultimonum = numero % 10
        resto = numero // 10
        return ultimonum + sumar_digitos(resto)

num = int(input("Ingrese su numero de mas de 1 digito: ")) 
while num < 10:
    num = int(input("Ingrese su numero de mas de 1 digito: ")) 
    
resultado = sumar_digitos(num)
print (f"la suma de los digitos de {num} es: {resultado}")
      