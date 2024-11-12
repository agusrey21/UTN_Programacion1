def cadena_invertida(cade):
    cade_invertida = cade[::-1]
    
    return cade_invertida

cadena = "hola mundo"
invertido = cadena_invertida(cadena)
print(invertido)

def contar(cade):
    palabras = cade.split()
    
    cant_palabras = len(palabras)
    return cant_palabras

contador = contar(cadena)
print(contador)

def reemplazar(cade, original, cambio):
    cadena_nueva = cade.replace(original, cambio)
    
    return cadena_nueva

origi = "mundo"
camb = "world"
reemplazo = reemplazar(cadena, origi, camb)
print(reemplazo)

def recomendar_pelis(lista):
    recomendaciones = []
    for pelis in lista:
        peliculas_str = ", ".join(pelis[:-1]) + " y " + pelis[-1]
        recomendacion = (f"Se recomienda ver \"{peliculas_str}\"")
        recomendaciones.append(recomendacion)
    return recomendacion
    
lista_peli = [
    ["Matrix", "El Padrino", "Titanic"],
    ["Forrest Gump", "Pulp Fiction", "Gladiador"], 
    ["Blade Runner", "El Rey León", "Volver al Futuro"], 
    ["La La Land", "El Gran Lebowski", "Blade Runner"], 
    ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
    ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
    ["Titanic", "Star Wars", "El Señor de los Anillos"], 
    ["The Truman Show", "The Shape of Water", "The Big Lebowski"], 
    ["Forrest Gump", "The Godfather", "Goodfellas"],
    ["The Terminator", "The Sixth Sense", "The Great Gatsby"]]

resultado = recomendar_pelis(lista_peli)
print(resultado)

def capitalizar(cadena):
    palabras = cadena.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    cadena_capi = " ".join(palabras_capitalizadas)
    return cadena_capi

cade = "hola como estas necesito estudiar."
resultado = capitalizar(cade)
print(resultado)

def palindromo(cadena):
    reversa = "".join(reversed(cadena))
    if cadena == reversa:
        return True

palabra = "oso"
resultado = palindromo(palabra)
if resultado == True:
    print(f"{palabra} es un palindromo.")
else:
    print(f"{palabra} no es un palindromo.")
    
def ordenar(string, numero):
    lista_caracteres = list(string)
    n = len(lista_caracteres)
    
    for i in range(1, n):
        clave = lista_caracteres[i]
        j = i - 1
        while j >= 0 and ((lista_caracteres[j] > clave and numero == 1) or (lista_caracteres[j] < clave and numero == -1)):
            lista_caracteres[j + 1] = lista_caracteres[j]
            j -= 1
        lista_caracteres[j + 1] = clave

    return ''.join(lista_caracteres)  

cadena = "hola como estas vamos a ordenar"
num = int(input("Ingrese 1 para ordenar de forma ascendente y -1 de forma descendente: "))
while num != 1 and num != -1:
    num = int(input("Ingrese 1 para ordenar de forma ascendente y -1 de forma descendente: "))
ordenado = ordenar(cadena, num)
print(ordenado)