class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método saludar()
persona1.saludar()


class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")

# Crear un objeto de la clase Libro
libro1 = Libro("Retorica", "Aristoteles", "347 a. C")

# Mostrar la información del libro
libro1.mostrar_informacion()


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Crear un objeto de la clase Rectangulo
rectangulo1 = Rectangulo(5, 3)

# Calcular y mostrar el área y el perímetro
area = rectangulo1.calcular_area()
perimetro = rectangulo1.calcular_perimetro()

print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)


class Calculadora:
    def __init__(self):
        pass

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            return "No se puede dividir por cero"
        else:
            return num1 / num2

# Crear un objeto de la clase Calculadora
calculadora = Calculadora()

# Realizar operaciones y mostrar resultados
resultado_suma = calculadora.sumar(5, 3)
resultado_resta = calculadora.restar(10, 4)
resultado_multiplicacion = calculadora.multiplicar(2, 6)
resultado_division = calculadora.dividir(8, 2)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# Crear objetos de las clases
perro1 = Perro("Firulais")
gato1 = Gato("Michi")

# Mostrar los sonidos
perro1.hacer_sonido()
gato1.hacer_sonido()


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Encapsulamiento del atributo titular
        self.__saldo = saldo_inicial  # Encapsulamiento del atributo saldo

    def obtener_saldo(self):
        print(f"El saldo actual de {self.__titular} es: {self.__saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Depósito realizado con éxito.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro realizado con éxito.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

# Crear una cuenta bancaria
cuenta1 = CuentaBancaria("Juan Pérez", 1000)

# Obtener el saldo
cuenta1.obtener_saldo()

# Realizar un depósito
cuenta1.depositar(500)

# Realizar un retiro
cuenta1.retirar(200)