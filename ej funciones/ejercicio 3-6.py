#Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
#solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
#dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
#por pantalla. Atención: pueden reutilizarse funciones ya creadas.
def realizarDescuento(numero):
  descuento = numero * 0.05
  return numero - descuento


numero1 = int(input("Ingrese un número entre 10 y 100: "))
while numero1 < 10 or numero1 > 100:
    numero1 = int(input("Ingrese un número entre 10 y 100: "))

resultado = realizarDescuento(numero1)
print(f"El valor con el descuento del 5% es: {resultado}")
    