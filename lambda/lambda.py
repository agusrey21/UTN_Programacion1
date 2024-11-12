print("El sueldo con el aumento de 10% pasa a ser: ")
print((lambda sueldo: sueldo * 1.1 )(100))


print((lambda edad: "es MAYOR" if edad > 17 else "es MENOR")(16))

print((lambda num: "ES PAR" if num %2 == 0 else "ES INPAR")(2))

print((lambda num: "POSITIVO" if num > 0 else "NEGATIVO")(-5))

descuento = 100 * 0.10
print((lambda sueldo, descuento: sueldo - descuento)(100, descuento))

print((lambda num: num * 2)(8))

valor = input("F o M: ").lower
while valor != "f" and valor != "m":
    valor = input("F o M: ").lower

print((lambda valor: "femenino" if valor == "f" else "masculino")(valor))
