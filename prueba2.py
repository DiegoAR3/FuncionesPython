#funciones

def mostrar_menu():
    print("==========Menú Principal==========")
    print("||1.- agregar reserva ||")
    print("||2.- buscar reserva ||")
    print("||3.- eliminar reserva ||")
    print("||4.- confirmar reservas ||")
    print("||5.- mostrar reservas ||")
    print("||6.- salir ||")
    print("=====================")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 6:
                raise ValueError
            else:
                return opcion
        except ValueError:
            print("Error, debe ingresar un numero del 1 al 6")

def agregar_reserva(lista_r):
    nombre_completo =input("ingrese su nombre completo: ")
    correcto = validar_huesped(nombre_completo)
    if not correcto:
        print("El nombre no puede estar vacío")
        return
    
    numero_habitacion = input("ingrese el numero de habitacion: ")
    correcto = validar_habitacion(numero_habitacion)
    if not correcto:
        print("la habitacion debe ser un numero entero entre 1 y 200")
        return
    cant_noches = input("ingrese el numero de noches que estará: ")
    correcto = validar_noches(cant_noches)
    if not correcto:
        print("la cantidad de noches debe ser mayor a 0")
        return
    #agregamos al diccionario

    reserva = {
        "huesped": nombre_completo.strip().upper(),
        "habitacion": int(numero_habitacion),
        "noches": int(cant_noches),
        "confirmada" : False
    }

    lista_r.apped(reserva)
    print("Reserva agregada correctamente")

def buscar_reserva(lista_r,huesped):
    for x in range(len(lista_r))
        if huesped == lista_r[x]["huesped"]:
            return x       
    return -1

def confirmar_reserva(lista_r):
    for r in lista_r:
        if r["noches"] >= 2:
            r["confirmada"] = True
        else:
            r["confirmada"] = False

def mostrar_reservas(lista_r):
    print("=====Lista de reservas=====")
    for r in lista_r:
        print(f"huesped: {r["huesped"]}")
        print(f"habitacion: {r["habitacion"]}")
        print(f"noches: {r["noches"]}")
        print(f"huesped: {r["huesped"]}")
        estado = "CONFIRMADA" if r["confirmada"] else "PENDIENTE"
        print(f"estado de reserva: {estado}")
        
#funciones de validaciones
def validar_huesped(nombre):
    return nombre.strip() != ""

def validar_habitacion(hab):
    if hab.isdigit():
        validar = int(hab)
        return validar >= 1 and validar <= 200
    return False

def validar_noches(noches):
    if  noches.isdigit():
        validar = int(noches)
        return validar > 0
    return False

#codigo principal
op = 0
while op != 6:
    mostrar_menu()

    op = ingresar_opcion()





