from ListaGramaticas import *
listaglc = ListaGramatica()
import time
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

        elif opcion == '3':
            print('Las gramaticas disponibles son: ')
            listaglc.MostrarGramaticas()
            eleccion = input('Ingrese el nombre de la gramatica de la cual desea su automata equivalente...')
            automata = listaglc.DevolverADP(eleccion)
            automata.AutomataEquivalente()
            input('Presione Enter para continuar...')

            print('Ocurrio un error inesperado')

def conteo(numero):
    num = int(numero)
    for i in range(num):
        numer = i + 1
        print(str(numer).center(100, ' '))
        time.sleep(1)


def PantallaInicial():
    print('╔═╗╦═╗╔═╗╔╦╗╔═╗╔╦╗╦╔═╗╔═╗╔═╗  ╦  ╦╔╗ ╦═╗╔═╗╔═╗  ╔╦╗╔═╗╦    ╔═╗╔═╗╔╗╔╔╦╗╔═╗═╗ ╦╔╦╗╔═╗'.center(60, ' '))
    print('║ ╦╠╦╝╠═╣║║║╠═╣ ║ ║║  ╠═╣╚═╗  ║  ║╠╩╗╠╦╝║╣ ╚═╗   ║║║╣ ║    ║  ║ ║║║║ ║ ║╣ ╔╩╦╝ ║ ║ ║'.center(60, ' '))
    print('╚═╝╩╚═╩ ╩╩ ╩╩ ╩ ╩ ╩╚═╝╩ ╩╚═╝  ╩═╝╩╚═╝╩╚═╚═╝╚═╝  ═╩╝╚═╝╩═╝  ╚═╝╚═╝╝╚╝ ╩ ╚═╝╩ ╚═ ╩ ╚═╝'.center(60, ' '))
    print(' ╔╗  ╦ ╔═╗ ╔╗╔ ╦ ╦ ╔═╗ ╔╗╔ ╦ ╔═╗ ╔╦╗ ╔═╗ '.center(60, ' '))
    print(' ╠╩╗ ║ ║╣  ║║║ ║ ║ ║╣  ║║║ ║ ║ ║  ║║ ║ ║ '.center(60, ' '))
    print(' ╚═╝ ╩ ╚═╝ ╝╚╝ ╚═╝ ╚═╝ ╝╚╝ ╩ ╚═╝ ═╩╝ ╚═╝ '.center(60, ' '))
    print('Kevin Raul Pozuelos Estrada'.center(100, ' '))
    print('CARNET: 201800992'.center(100, ' '))
    conteo(5)
    print('╔╦╗╔═╗╔╗╔╦ ╦  ╔═╗╦═╗╦╔╗╔╔═╗╦╔═╗╔═╗╦  '.center(70, ' '))
    print('║║║║╣ ║║║║ ║  ╠═╝╠╦╝║║║║║  ║╠═╝╠═╣║  '.center(70, ' '))
    print('╩ ╩╚═╝╝╚╝╚═╝  ╩  ╩╚═╩╝╚╝╚═╝╩╩  ╩ ╩╩═╝'.center(70, ' '))
    os.system('cls')






