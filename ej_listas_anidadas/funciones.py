def producto_nuevo(inventario: list, producto: str, cantidad: int, fila:int, colu:int):
    inventario.append({"producto": producto, "cantidad": cantidad, "fila": fila, "columna": colu})
    print(f"Producto {producto} agregado con exito.")
    
def producto_existente(inventario: list, producto: str):
    for i, item in enumerate(inventario):
        if item["producto"] == producto:
            inventario.pop(i)
            print("Producto eliminado.")
            return
    print(f"Producto {producto} eliminado. ")
    
def cant_ubicacion(inventario:list, rt:int, producto:str):
    if rt == 1:
        print("Desea cambiar la ubicacion.")
        fila = int(input("En que fila la desea? "))
        columna = int(input("En que columna la desea? "))
        for i, item in enumerate(inventario):
            if item["producto"] == producto:
                item["fila"] = fila
                item["columna"] = columna
    elif rt == 2:
        print("Desea modificar la cantidad.")
        cant = int(input("Ingrese la cantidad nueva del producto: "))
        for i, item in enumerate(inventario):
            if item["producto"] == producto:
                item["cantidad"] = cant
    else:
        fila = int(input("En que fila la desea? "))
        columna = int(input("En que columna la desea? "))
        cant = int(input("Ingrese la cantidad nueva del producto: "))
        for i, item in enumerate(inventario):
            if item["producto"] == producto:
                item["fila"] = fila
                item["columna"] = columna
                item["cantidad"] = cant
        
def lista_produ(inventario):
    print("Inventario: ")
    for i in inventario:
        print(f"Producto: {i["producto"]}, Cantidad: {i["cantidad"]}, fila: {i["fila"]}, columna: {i["columna"]}")
        
def orden_por_nombre(inventario):
    print("Inventario: ")
    for i in range(len(inventario) - 1):
        for j in range(len(inventario) - i - 1):
            if inventario[j]["producto"] > inventario[j+1]["producto"]:
                aux = inventario[j]
                inventario[j] = inventario[j+1]
                inventario[j+1] = aux
    for i in inventario:
        print(f"Producto: {i["producto"]}, Cantidad: {i["cantidad"]}, fila: {i["fila"]}, columna: {i["columna"]}")


