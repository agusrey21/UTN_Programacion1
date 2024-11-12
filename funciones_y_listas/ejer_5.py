def edades_min(edades):
    
    minima = min(edades)
    print(minima)
    indices = []
    for i, edad  in enumerate(edades):
        if edad == minima:
            indices.append(i)
    
    return indices



nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio","Eugenia","Soledad","Mario","Mariela"]
edad = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

resultado = edades_min(edad)
print("Los indices de las personas con menor edad son: ", resultado)
for i in resultado:
    print(nombres[i])