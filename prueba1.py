#funciones
def mostrar_menu():
    print("==========Menú Principal==========")
    print("||1.- agregar mascota ||")
    print("||2.- buscar mascota ||")
    print("||3.- eliminar mascota ||")
    print("||4.- marcar como vacunada ||")
    print("||5.- mostrar mascota ||")
    print("||6.- salir ||")
    print("=====================")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 6:
                print("Debe ingresar un numero del 1 al 6")
            else:
                break
        except ValueError:
            print("Error, debe ingresar un numero")
    return opcion

#codigo principal

#declarar lista

lista_mascotas = []
op = 0
while op != 6:
    mostrar_menu()

    op = ingresar_opcion()
