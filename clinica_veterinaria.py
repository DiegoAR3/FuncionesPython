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
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sistema, vuelva pronto")
