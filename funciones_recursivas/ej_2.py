def calcular_potencia(base: int, exponente: int)-> int:
    if exponente == 0:
        return 1
    else:
        print(base**exponente)
        return calcular_potencia(base, exponente - 1)
    
base = int(input("Ingrese su base: "))
exponente = int(input("Ingrese su exponente: "))
resultado = calcular_potencia(base, exponente)
print("resultado")
print(f"esos son los resultados de {base}^{exponente}")