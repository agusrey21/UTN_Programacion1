gondola = [
    [{"producto": "botellas", "cantidad": 3, "ubicacion": (1, 2)}],
    [{"producto": "fideos", "cantidad": 4, "ubicacion": (2, 1)}],
    [{"producto": "leche", "cantidad": 6, "ubicacion": (3, 1)}],
    [{"producto": "frascos", "cantidad": 8, "ubicacion": (1, 4)}]
]
print(gondola)
def mostrar_inventario():
    for fila in gondola:
        for producto in fila:
            print(f"Producto: {producto['producto']}, Cantidad: {producto['cantidad']}, Ubicación(Fila, Columna): {producto['ubicacion']}")

mostrar_inventario()


    