def MenuPrincipal():
    print('INGRESE EL NUMERO DE LA ACCION QUE DESEA REALIZAR'.center(70, ' '))
    print(' '.ljust(9, ' '), '1) Cargar archivo')
    print(' '.ljust(9, ' '), '2) Mostrar informacion general de la gramatica')
    print(' '.ljust(9, ' '), '3) Generar automata de pila equivalente')
    print(' '.ljust(9, ' '), '4) Reporte de recorrido')
    print(' '.ljust(9, ' '), '5) Reporte de tabla')
    print(' '.ljust(9, ' '), '6) Salir del programa')
    opcion = input('Ingrese su opcion: '.rjust(29, ' '))

    if opcion == '1':

        return True

    elif opcion == '2':
        return True

    elif opcion == '3':
        return True

    elif opcion == '4':
        return True


    elif opcion == '5':
        return True

    elif opcion == 6:
        return False

    else:
        print("Opcion no valida, ingrese nuevamente la opcion deseada")


def cargarArchivo():
    try:
        ruta = input('Ingrese el nombre de su archivo con su extension .glc...')
        print(ruta)
    except:
        print('Ocurrio un error archivo erroneo')