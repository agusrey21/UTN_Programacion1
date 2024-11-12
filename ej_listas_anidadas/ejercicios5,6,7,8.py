#ej5 
cajonera = [
    [{"mm": "to12", "cantidad": 65, "fila": (1), "cajon": (1)}],
    [{"mm": "to16", "cantidad": 86, "fila": (1), "cajon": (2)}],
    [{"mm": "to20", "cantidad": 65, "fila": (1), "cajon": (3)}],
    [{"mm": "to25", "cantidad": 45, "fila": (1), "cajon": (4)}],
    [{"mm": "to30", "cantidad": 68, "fila": (2), "cajon": (1)}],
    [{"mm": "to35", "cantidad": 73, "fila": (2), "cajon": (2)}],
    [{"mm": "to40", "cantidad": 85, "fila": (2), "cajon": (3)}],
    [{"mm": "to45", "cantidad": 89, "fila": (2), "cajon": (4)}],
    [{"mm": "ta4", "cantidad": 58, "fila": (3), "cajon": (1)}],
    [{"mm": "ta5", "cantidad": 48, "fila": (3), "cajon": (2)}],
    [{"mm": "ta6", "cantidad": 64, "fila": (3), "cajon": (3)}],
    [{"mm": "ta7", "cantidad": 96, "fila": (3), "cajon": (4)}],
    [{"mm": "ta8", "cantidad": 36, "fila": (4), "cajon": (1)}],
    [{"mm": "ta10", "cantidad": 72, "fila": (4), "cajon": (2)}],
    [{"mm": "ta12", "cantidad": 78, "fila": (4), "cajon": (3)}],
    [{"mm": "ta14", "cantidad": 71, "fila": (4), "cajon": (4)}]
    ]

def reponer(cajonera:list, producto:str, cantidad:int):
    for i in cajonera:
        for cajon in i:
            if cajon["mm"] == producto:
                cajon["cantidad"] += cantidad
                return
    print("No se encuentra el producto solicitado.")
    
def venta(cajonera:list, producto:str, cantidad:int):
    for i in cajonera:
        for cajon in i:
            if cajon["mm"] == producto:
                cajon["cantidad"] -= cantidad
                return
    print("No se encuentra el producto solicitado.")
    

def listar(cajonera:list):
    print("cajonera: ")
    for i, cajon in enumerate(cajonera):
        for item in cajon:
            print(f"Producto: {item["mm"]}, Cantidad: {item["cantidad"]}, fila: {item["fila"]}, cajon: {item["cajon"]}")
        
        
while True:
    print("--------------------------------------------")
    print("                MENU                        ")
    print("""
      1- Reponer mercadería (productos existentes)
        2- Vender mercadería (producto existente, solo si alcanza el stock)
            3- Listar inventario
                5- Salir""")
    print("--------------------------------------------")
    
    opcion = int(input("¿Que desea hacer?: "))
    
    match opcion:
        case 1: 
            produ = input("¿Que producto desea reponer?: ")
            cant = int(input("¿Cuanto repone?: "))
            reponer(cajonera, produ, cant)
        case 2:
            produ = input("¿Que producto vende?: ")
            cant = int(input("¿cuanto vendio?: "))
            venta(cajonera, produ, cant)
        case 3:
            listar(cajonera)
        case 5:
            print("Saliendo del programa.")
            break
        case _:
            print("Ingrese una opcion correcta.")
    