import os

def limpiar_pantalla():
    os.system("cls")

def mostrar_menu():
    print("""
MENU PRINCIPAL
--------------
1. Agregar producto.
2. Buscar producto.
3. Eliminar producto.
4. Salir.
""")

def obtener_opcion():
    opcion = input("Seleccione la opcion: ")
    return opcion

def obtener_datos_producto(productos):
    limpiar_pantalla()
    print("MENU OBTENER DATOS DE PRODUCTO")
    print("------------------------------")
    
    print(f"Los productos actuales son: {productos}")

    while True:
        nombre = input("Nombre: ")

        if len(productos) == 0:
            break

        repetido = False
        for producto in productos:
            if nombre == producto[0]:
                repetido = True
                input("El nombre no puede estar repetido <ENTER>")
                break

        if repetido == False:
            break

    while True:
        categoria = input('categoria ("Electronica", "Muebles" o "Ropa"): ')
        if categoria in ["Electronica", "Muebles", "Ropa"]:
            break
        else:
            input("Categoria incorrecta <ENTER>")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad >= 0:
                break
            else:
                input("La cantidad debe ser mayor o igual a 0 <ENTER>")
        except:
            input("La cantidad debe ser un numero <ENTER>")

    return nombre, categoria, cantidad

def buscar_producto(productos):
    limpiar_pantalla()
    print("BUSCAR PRODUCTO")
    print("---------------")
    nombre = input("Nombre del producto a buscar: ")

    for producto in productos:
        if producto[0] == nombre:
            input(f"Categoria: {producto[1]}, Cantidad: {producto[2]} <ENTER>")
            return

    input("El producto no se encuentra <ENTER>")

def eliminar_producto(productos):
    limpiar_pantalla()
    print("ELIMINAR PRODUCTO")
    print("------------------")
    nombre = input("Nombre del producto a eliminar: ")

    for i in range(len(productos)):
        if productos[i][0] == nombre:
            input("Producto eliminado! <ENTER>")
            return

    input("No se pudo eliminar el producto! <ENTER>")

productos = []

while True:
    limpiar_pantalla()
    mostrar_menu()
    opcion = obtener_opcion()

    if opcion == "1":
        nombre, categoria, cantidad = obtener_datos_producto(productos)
        productos.append([nombre, categoria, cantidad])
        input(f"Los productos actuales son: {productos} <ENTER>")

    elif opcion == "2":
        buscar_producto(productos)

    elif opcion == "3":
        eliminar_producto(productos)

    elif opcion == "4":
        input("Saliendo... <ENTER>")
        break

    else:
        input("Opcion invalida <ENTER>")


print("\nAdios!")
