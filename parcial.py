def crear_paciente():
    """Crea un nuevo paciente y lo agrega a la lista."""
    historia_clinica = int(input("Ingrese el número de historia clínica: "))
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    diagnostico = input("Ingrese el diagnóstico: ")
    dias_internacion = int(input("Ingrese la cantidad de días de internación: "))
    return [historia_clinica, nombre, edad, diagnostico, dias_internacion]

def mostrar_pacientes(pacientes):
    """Muestra la lista completa de pacientes."""
    print("Lista de pacientes:")
    for paciente in pacientes:
        print(f"Historia clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")

def buscar_paciente(pacientes, historia_clinica):
    """Busca un paciente por su número de historia clínica."""
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            print(f"Paciente encontrado: {paciente}")
            return
    print("Paciente no encontrado.")

def ordenar_pacientes(pacientes):
    """Ordena a los pacientes por número de historia clínica."""
    for i in range(len(pacientes) - 1):
        for j in range(len(pacientes) - i - 1):
            if pacientes[j][0] > pacientes[j+1][0]:
                aux = pacientes[j]
                pacientes[j] = pacientes[j+1]
                pacientes[j+1] = aux
    print("Pacientes ordenados por historia clínica.")

def paciente_mas_dias(pacientes):
    """Encuentra el paciente con más días de internación."""
    max_dias = 0
    paciente_max_dias = None
    for paciente in pacientes:
        if paciente[4] > max_dias:
            max_dias = paciente[4]
            paciente_max_dias = paciente
    print(f"Paciente con más días de internación:\n{paciente_max_dias}")

def promedio_dias_internacion(pacientes):
    """Calcula el promedio de días de internación."""
    total_dias = 0
    for i in pacientes:
        total_dias += i[4]
    promedio = total_dias / len(pacientes)
    print(f"Promedio de días de internación: {promedio:.2f}")


pacientes = []

while True:
    print("Sistema de Gestión de Clínica")
    print("1. Cargar pacientes")
    print("2. Mostrar pacientes")
    print("3. Buscar paciente")
    print("4. Ordenar pacientes")
    print("5. Paciente con más días de internación")
    print("6. Promedio de días de internación")
    print("7. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        while True:
            pacientes.append(crear_paciente())
            continuar = input("¿Desea cargar otro paciente? (s/n): ")
            while continuar.lower() != 's' and continuar.lower() != 'n':
                continuar = input("¿Desea cargar otro paciente? (s/n): ")
            if continuar.lower() == 'n':
                break
    elif opcion == 2:
        mostrar_pacientes(pacientes)
    elif opcion == 3:
        historia_clinica = int(input("Ingrese el número de historia clínica a buscar: "))
        buscar_paciente(pacientes, historia_clinica)
    elif opcion == 4:
        ordenar_pacientes(pacientes)
    elif opcion == 5:
        paciente_mas_dias(pacientes)
    elif opcion == 6:
        promedio_dias_internacion(pacientes)
    elif opcion == 7:
        break
    else:
        print("Opción inválida.")