import prueba2 as p

#codigo principal
lista_reservas = []
op = 0
while op != 6:
    p.mostrar_menu()

    op = p.ingresar_opcion()

    if op == 1:
        #llamar a la funcion que ingresa nuevas reservas
        p.agregar_reserva(lista_reservas)
    elif op == 2:
        #solicitamos el nombre a buscar
        nombre = input("ingrese el nombre del huesped a buscar: ")
        #llamamos a la funcion encargada de buscar
        posicion = p.buscar_reserva(lista_reservas,nombre)
        #validamos que retorna la funcion de buscar
        if posicion !=-1:
            #se encontró el huesped aso que muestro sus datos
            print("********reserva encontrada********")
            print(f"Nombre del huesped: {lista_reservas[posicion]["huesped"]}")
            print(f"Numero de habitacion: {lista_reservas[posicion]["habitacion"]}")
            print(f"Noches hospedadas: {lista_reservas[posicion]["noches"]}")
            estado = "CONFIRMADA" if lista_reservas[posicion]["confirmada"] else "PENDIENTE"
            print(f"Estado: {estado}")
            print("******************************************")
        else:
            print(f"El huesped {nombre} no ha sido encontrado")

    elif op == 3:
        nombre = input("ingrese el nombre del huesped a eliminar")
        posicion = p.buscar_reserva(lista_reservas,nombre)
        if posicion !=-1:
            lista_reservas.pop(posicion)
            print("reserva eliminada correctamente")
        else:
            print(f"El huesped {nombre} no ha sido encontrado")


    elif op == 4:
        p.confirmar_reserva(lista_reservas)
        print("Reservas Actualizadas")
    elif op == 5:
        p.confirmar_reserva(lista_reservas)
        p.mostrar_reservas(lista_reservas)
    
print("gracias por usar el sistema, hasta luego")