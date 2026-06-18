#funciones
#validaciones
def validar_nombre(name):
    #funcion de python que elimina los espacios al inicio o al final de un string y si queda vacia devuelve un false
    return name.strip() != "" #Retorna True si es valido - False si es invalido
def validar_especie(especie):
    #verificar que es perro, gato o ave (sin diferenciar mayusculas o minusculas)
    especies_validas = ["perro", "gato", "ave"]
    return especie.strip().lower() in especies_validas
def validar_edad(edad):
    #validar que sean numero y mayor a cero
    return edad.isdigit() and int(edad) > 0


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
#funcion para agregar una mascota nueva
def agregar_mascota(lista):
    nombre = input("ingrese el nombre de la mascota: ")
    #llamar la funcion que valida el nombre para mostrar el mensaje
    correcto = validar_nombre(nombre)
    if not correcto:
        print("el nombre no puede estar vacio")
        return
    especie = input("ingrese la especie de la mascota(perro, gato o ave): ")
    correcto = validar_especie(especie)
    if not correcto:
        print("la especie solo puede ser perro, gato o ave")
        return
    edad = input("ingrese la edad de la mascota: ")
    correcto = validar_edad(edad)
    if not correcto:
        print("deber ser un numero valido mayor a cero")
        return
    #aqui agrego al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    #agrego a la lista
    lista.append(mascota)
    print("mascota agregada correctamente")

def buscar_mascota(lista_m, nombre_m):
    #recorrer la lista
    for x in range(len(lista_m)):
        #verificamos si el nombre coincide
        if nombre_m == lista_m[x]["nombre"]:
            return x #retorno la posicion
    #si no lo encuentro
    return -1 
def actualizar_vacunas(lista_m):
    for m in lista_m:
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
#codigo principal

#declarar lista

lista_mascotas = []
op = 0
while op != 6:
    mostrar_menu()

    op = ingresar_opcion()

    if op == 1:
        agregar_mascota(lista_mascotas)
    elif op == 2:
        nombre = input("ingrese el nombre de la mascota a buscar: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        #validar que devolvio la funcion
        if posicion != -1: #la encontró
            print(f"la posicion encontrada es: {posicion + 1}")
            #almacenar el diccionario en una variable
            m = lista_mascotas[posicion]
            print(f"Nombre mascota: {m["nombre"]}")
            print(f"especie mascota: {m["especie"]}")
            print(f"edad mascota: {m["edad"]}")
            print(f"Vacunada: {m["vacunada"]}")
        else:
            print("la mascota no se ha encontrado")
    elif op == 3:
        nombre = input("ingrese el nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        #validar que devolvio la funcion
        if posicion != -1: #la encontró
            lista_mascotas.pop(posicion)
            print("la mascota ha sido eliminada de la lista")
        else:
            print(f"la mascota {nombre} no se encuentra en la lista")
    elif op == 4:
        actualizar_vacunas(lista_mascotas)
        print("Vacunas actualizadas")
    elif op == 5:
        #actualizar las vacunas
        actualizar_vacunas(lista_mascotas)
        #mostrar datos de las mascotas
        if len(lista_mascotas) == 0:
            print("no hay mascotas para mostrar")
        else:
            print("== lista mascotas ==")
            print(f"Nombre mascota: {m["nombre"]}")
            print(f"especie mascota: {m["especie"]}")
            print(f"edad mascota: {m["edad"]}")
            estado = "AL DIA" if m["vacunada"] else "PENDIENTE"
            print(f"estado de vacuna: {estado}")
            print("=============================")

    elif op == 6:
        print("Gracias por usar el sistema, vuelva pronto")
