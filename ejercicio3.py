#Funciones

def dato_productos (nombre, precio, stock):
    print("=======================")
    print(f"nombre del producto: {nombre}")
    print(f"precio: {precio}")
    print(f"stock: {stock}") 
    print("=======================")

#Código principal

nombre = input("ingrese el nombre del producto: ")
while True:
    try:
        Stock = int(input("ingrese el stock del producto: "))
        if Stock < 0:
            print("Deber ser mayor o igual a cero")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")


while True:
    try:
        precio = int(input("ingrese el precio del producto: "))
        if precio <= 0:
            print("Debe ser un numero positivo")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")


dato_productos(nombre, precio, Stock)
