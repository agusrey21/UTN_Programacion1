from funciones import *
inventario = []
while True:
    
    print("""
          1-Alta de productos (producto nuevo)
            2-Baja de productos (producto existente)
                3-Modificar productos (cantidad, ubicación)
                    4-Listar productos
                        5-Lista de productos ordenado por nombre
                            6-Salir""")
    
    opcion = int(input("Ingrese una opcion: "))
    
    match opcion:
        case 1:
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            fila = int(input("En que fila lo ubicas? "))
            columna = int(input("En que columna lo ubicas? "))
            producto_nuevo(inventario, producto, cantidad, fila, columna)
        case 2:
            if len(inventario) == 0:
                print("Ingrese los productos primero.")
            else:
                producto = input("Ingrese el producto que desea eliminar: ")
                producto_existente(inventario, producto)
        case 3:
            if len(inventario) == 0:
                print("Ingrese los productos primero.")
            else:
                producto = input("Que producto desea modificar? ")
                rt = int(input("desea cambiar la ubicacion, modificar la cantidad o ambas? (1, 2, 3) "))
                while rt != 1 and rt != 2 and rt != 3:
                    print("Presione una opcion correcte. (1, 2, 3)")
                    rt = input("desea cambiar la ubicacion, modificar la cantidad o ambas? (1, 2, 3) ")
                
                cant_ubicacion(inventario, rt, producto)
        case 4:
            lista_produ(inventario)
        case 5:
            orden_por_nombre(inventario)
        case 6:
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion incorrecta.")