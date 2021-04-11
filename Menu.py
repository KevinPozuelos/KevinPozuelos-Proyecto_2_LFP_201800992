from ListaGramaticas import *
listaglc = ListaGramatica()
def MenuPrincipal():
    print('INGRESE EL NUMERO DE LA ACCION QUE DESEA REALIZAR'.center(70, ' '))
    print(' '.ljust(9, ' '), '1) Cargar archivo')
    print(' '.ljust(9, ' '), '2) Mostrar informacion general de la gramatica')
    print(' '.ljust(9, ' '), '3) Generar automata de pila equivalente')
    print(' '.ljust(9, ' '), '4) Reporte de recorrido')
    print(' '.ljust(9, ' '), '5) Reporte de tabla')
    print(' '.ljust(9, ' '), '6) Salir del programa')
    opcion = input('Ingrese su opcion: '.rjust(29, ' '))
    return opcion

def menuP():

    while True:
        opcion = MenuPrincipal()
        if opcion == '1':
            ruta = input('Ingrese el nombre de su archivo con su extension .glc...')
            print(ruta)
            listaglc.CargarGramaticas(ruta)

        elif opcion == '2':
            print('Las gramaticas disponibles son: ')
            listaglc.MostrarGramaticas()
            eleccion = input('Ingrese el nombre de la gramatica que desea visualizar...')
            automata = listaglc.DevolverADP(eleccion)
            try:
                listaglc.ImprimirAutomata(automata)
                input('Presione Enter para continuar...')
                os.system('cls')
            except:
                print('No eligio un automata correcto')







