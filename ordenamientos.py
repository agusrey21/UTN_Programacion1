#ej 1
nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_por_nombre():
    for i in range(len(nombres) - 1):
        for j in range(len(nombres) - i - 1):
            if nombres[j] > nombres[j+1]:
                aux = nombres[j]
                nombres[j] = nombres[j+1]
                nombres[j+1] = aux
                aux_e = Edades[j]
                Edades[j] = Edades[j+1]
                Edades[j+1] = aux_e
                
    for i in range(len(nombres)):
        print("Nombre: ", nombres[i], "Edad: ", Edades[i], end=" ")
    print("")

resultado = ordenar_por_nombre()
print(resultado)

#2
Nombres_m = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_notas():
    for i in range(len(Nombres_m) - 1):
        for j in range(len(Nombres_m) - i - 1):
            if Nombres_m[j] > Nombres_m[j+1]:
                aux = Nombres_m[j]
                Nombres_m[j] = Nombres_m[j+1]
                Nombres_m[j+1] = aux
            if Nombres_m[j] == Nombres_m[j+1]:
                if Puntos[j] < Puntos[j+1]:
                    aux = Puntos[j]
                    Puntos[j] = Puntos[j+1]
                    Puntos[j+1] = aux
    
    for i in range(len(Nombres_m)):
        print("Nombre: ", Nombres_m[i], "puntos: ", Puntos[i])
    print("")
    
resultado = ordenar_notas()

#3
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def lista_apellidos():
    for i in range(len(Apellidos) - 1):
        for j in range(len(Apellidos) - i - 1):
            if Apellidos[j] > Apellidos[j+1]:
                aux1 = Apellidos[j]
                Apellidos[j] = Apellidos[j+1]
                Apellidos[j+1] = aux1
            if Apellidos[j] == Apellidos[j+1]:
                if Estudiantes[j] > Estudiantes[j+1]:
                    aux2 = Estudiantes[j]
                    Estudiantes[j] = Estudiantes[j+1]
                    Estudiantes[j+1] = aux2
                
                if Estudiantes[j] == Estudiantes[j+1]:
                    if Nota[j] < Nota[j+1]:
                        aux3 = Nota[j]
                        Nota[j] = Nota[j+1]
                        Nota[j+1] = aux3
    
    for i in range(len(Apellidos)):
        print("apellido: ", Apellidos[i], "| Nombre: ", Estudiantes[i], "| nota: ", Nota[i])
    print("")

resultado = lista_apellidos()