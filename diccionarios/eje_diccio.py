from estudiantes import estudiantes as alumnos

def ordenar(alumnos, datos):
    n = len(alumnos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if alumnos[j]["apellido"] > alumnos[j + 1]["apellido"]:
                aux = alumnos[j]
                alumnos[j] = alumnos[j + 1]
                alumnos[j + 1] = aux
    
    for alumno in alumnos:
        for dato in datos:
            print(f"{dato}: {alumno[dato]}", end= " ")
            
        print(" ")
    
def prom_notas(alumnos):
    contador = 0
    contador_notas = 0
    for alumno in alumnos:
        for nota in alumno["notas"]:
            contador_notas += 1
            contador += nota
            prom = contador/contador_notas
            print(f"el promedio de notas de {alumno["nombre"]} es: {prom}")

def listar(alumnos, datos):
    ingenieros = []
    for alumno in alumnos:
        carrera = alumno["programa"]["nombre"]
        if carrera == "Ingenieria en Informatica":
            ingenieros.append(alumno)
    
    print("Alumnos que estudian Ingenieria en Informatica: ")
    for alumno in ingenieros:
        for dato in datos:
            print(f"{dato}: {alumno[dato]}", end= " ")
        print(" ")

def prom_edad(alumnos, datos):
    contador = 0
    cant = 0
    for alumno in alumnos:
        cant += 1
        edad = alumno["edad"]
        contador += edad
    prom = contador/cant
    print(f"el promedio de edad es de: {prom}")
    
    print("alumnos: ")
    for alumno in alumnos:
        for dato in datos:
            print(f"{dato}: {alumno[dato]} ", end= " ")
        print(" ")

def mayor_prom(alumnos, datos):
    contador = 0
    contador_notas = 0
    prom_mayor = 0
    alumno_nota = {}
    for alumno in alumnos:
        for nota in alumno["notas"]:
            contador_notas += 1
            contador += nota
            prom = contador/contador_notas
            
        if prom > prom_mayor:
            prom_mayor = prom
            alumno_nota = alumno
            
    print("alumno con mejor promedio de nota: ")
    for dato in datos:
        print(f"{dato}: {alumno_nota[dato]} ", end= " ")
    print(" ")
            
def grupos(alumnos, datos):
    integrantes = []
    for alumno in alumnos:
        if "grupos" in alumno:
            for grupo in alumno["grupos"]:
                if grupo["nombre"] == "Club de Informatica":
                    integrantes.append(alumno)
                
                
    print("Alumnos que estan en el Club de Informatica: ")
    for alumno in integrantes:
        contador = 0
        contador_notas = 0
        for nota in alumno["notas"]:
            contador_notas += 1
            contador += nota
            prom = contador/contador_notas
        for dato in datos:
            print(f"{dato}: {alumno[dato]}", end= " ")
        print(f", su promedio es de: {prom}")
        print(" ")
    
def mas_jovenes(alumnos, datos):
    contador = 0
    cant = 0
    for alumno in alumnos:
        cant += 1
        contador += alumno["edad"]
    prom = contador/cant 
    
    for alumno in alumnos:
        if alumno["edad"] < prom:
            for dato in datos:
                print(f"{dato}: {alumno[dato]}", end= " ")
                   

def menu():
    while True:
    
        print("""Menu de opciones:
        1-Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre. Mostrar legajo, nombre, apellido y edad
        2-Obtener el promedio de notas para cada estudiante
        3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica”
        4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido
        5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido
        6-Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios
        7-Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.
        8-Salir
        """)
    
        opcion = int(input("Ingrese una opcion: "))
        while opcion < 1 or opcion > 8:
            opcion = int(input("Ingrese una opcion: "))
    
        match opcion:
            case 1:
                ordenar(alumnos, ["legajo","nombre","apellido", "edad"])
            case 2:
                prom_notas(alumnos)
            case 3:
                listar(alumnos, ["legajo", "nombre", "apellido", "edad"])
            case 4:
                prom_edad(alumnos, ["nombre", "apellido"])
            case 5:
                mayor_prom(alumnos, ["nombre", "apellido"])
            case 6:
                grupos(alumnos, ["nombre", "apellido"])
            case 7:
                mas_jovenes(alumnos, ["legajo","nombre","apellido", "programa"])
            case 8:
                print("Saliendo...")
                break
        
    

menu()
