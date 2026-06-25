def validar_jugador(nombre):
    return nombre.strip() != ""

def validar_juego(juego):
    return juego.strip() != ""

def validar_puntos(puntos):
    if puntos.isdigit():
        validar = int(puntos)
        return validar > 0
    return False
    
def mostrar_menu():
    print("==========Menú Principal==========")
    print("||1.- registrar jugador ||")
    print("||2.- buscar buscar jugador ||")
    print("||3.- eliminar jugador ||")
    print("||4.- actualizar clasificacion ||")
    print("||5.- mostrar juadores ||")
    print("||6.- salir ||")
    print("=====================")


def ingresar_opcion():
    while True:
        try:
            opcion = int(input("ingrese una opcion: "))
            if opcion > 6 or opcion < 1:
                raise ValueError
            else:
                return opcion
        except ValueError:
            print("debe ingresar un numero del 1 al 6")

def agregar_jugador(lista_j):
    nombre_jugador = input("ingrese su nombre de jugador: ")
    correcto = validar_jugador(nombre_jugador)
    if not correcto:
        print("el nombre no puede estar vacio")
        return
    
    juego = input("ingrese el juego: ")
    correcto = validar_juego(juego)
    if not correcto:
        print("el juego no puede estar vacio")
        return
    
    punto = input("ingrese sus puntos: ")
    correcto = validar_puntos(punto)
    if not correcto:
        print("los puntos deben ser un numero entero")
        return
    
    inscripcion = {
        "nombre": nombre_jugador.strip().lower(),
        "juego": juego.strip().lower(),
        "puntos": int(punto),
        "clasificado": False

    }
    lista_j.append(inscripcion)
    print("inscripcion agregada correctamente")
    return

def buscar_jugador(lista_j,nombre_j):
    for x in range(len(lista_j)):
        if nombre_j.strip().lower() == lista_j[x]["nombre"].strip().lower():
            return x
    return -1


def actualizar_clasificacion(lista_j):
    for j in lista_j:
        if j["puntos"] >=1000:
            j["clasificado"] = True
        else:
            j["clasificado"] = False

def mostrar_jugador(lista_j):
    for j in lista_j:
        print(f"nombre de jugador {j["nombre"]}")
        print(f"juego: {j["juego"]}")
        print(f"puntaje: {j["puntos"]}")
        estado = "clasificado" if j["clasificado"] else "no clasificado"
        print (f"estado de jugador: {estado}")


lista_jugadores = []
op = 0
while op !=6:
    mostrar_menu()

    op = ingresar_opcion()


    if op == 1:
        agregar_jugador(lista_jugadores)
    elif op == 2:
        nombre = input("ingrese el nombre del jugador a buscar: ")
        for j in lista_jugadores:
            posicion = buscar_jugador(lista_jugadores,nombre)
            if posicion != -1:
                print(f"nombre de jugador {j["nombre"]}")
                print(f"juego: {j["juego"]}")
                print(f"puntaje: {j["puntos"]}")
                estado = "clasificado" if j["clasificado"] else "no clasificado"
                print (f"estado de jugador: {estado}")
            else:
                print(f"el jugador llamado {nombre} no se encuentra")
    elif op == 3:
        nombre = input("ingrese el nombre del jugador a eliminar: ")
        posicion = buscar_jugador(lista_jugadores, nombre)
        if posicion != -1:
            lista_jugadores.pop(posicion)
            print("jugador eliminado correctamente")

        else:
            print(f"el jugador {nombre} no se ha encontrado")

    elif op == 4:
        actualizar_clasificacion(lista_jugadores)
        print("clasificacion actualizada")

    elif op == 5:
        actualizar_clasificacion(lista_jugadores)
        mostrar_jugador(lista_jugadores)
    elif op == 6:
        print("hasta luego")