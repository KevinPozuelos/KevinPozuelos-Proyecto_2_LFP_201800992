from AutomataPila import *


class ListaAutomatas(object):
    def __init__(self):
        self.automatas = []

    def ExisteAFD(self, AFD):
        for afd in self.automatas:
            if afd.nombre == AFD:
                print('Existe un automata con ese nombre')
                return True
        return False

    def EstaVacio(self):
        if len(self.automatas) == 0:
            return True
        else:
            return False

    def EliminarAFD(self, nombre):
        for afd in self.automatas:
            if afd.nombre == nombre:
                self.automatas.remove(afd)
                print('Automata eliminado')

    def Espacios(self):
        print('')
        print('')

    def Agregar(self, AFD):
        if not self.ExisteAFD(AFD.nombre):
            self.automatas.append(AFD)
        else:
            '''Ya se manda mensaje desde el otro metodo'''

    def MostrarAPs(self):
        for afd in self.automatas:
            print(afd.nombre)

    def CargarAFDs(self, ruta):
        automatas = open(ruta, 'r')
        noL = 0  # Numero de linea
        for linea in automatas.readlines():
            noL += 1
            linea = linea.replace('\n', '')

            if noL == 1:  # Ingresando titulo al automata
                if not self.ExisteAFD(linea):
                    EnCreacion = AutomataPila(linea)
                    print(EnCreacion.nombre, 'creandose')
                else:
                    self.EliminarAFD(linea)
                    EnCreacion = AutomataPila(linea)
                    print(EnCreacion.nombre, 'creandose')
            elif noL == 2:  # Ingresando estados al automata
                for alfa in linea.split(','):
                    EnCreacion.IngresarAlfabeto(alfa)
                EnCreacion.cadenaAlfabeto = linea
            elif noL == 3:  # Ingresando alfabeto del automata
                for alfa in linea.split(','):
                    EnCreacion.IngresarSimbolos(alfa)
                EnCreacion.cadenaSimbolos = linea
            elif noL == 4:  # Ingresando estado inicial
                for estado in linea.split(','):
                    EnCreacion.AgregarEstados(estado)
                EnCreacion.cadenaEstados = linea
            elif noL == 5:  # Agregando estados de aceptacion
                EnCreacion.inicial = linea
            elif noL == 6:  # Agregando estados de aceptacion
                EnCreacion.aceptacion = linea
            elif linea == '*':
                print(' ')
                self.automatas.append(EnCreacion)
                print('Automata agregado correctamente')
                self.ImprimirAutomata(EnCreacion)
                self.Espacios()
                noL = 0
            else:
                EnCreacion.AgregarTransicion(linea)
        automatas.close()

    def DevolverADP(self, nombre):
        for adp in self.automatas:
            if adp.nombre == nombre:
                return adp
        return False

    def ImprimirAutomata(self, EnCreacion):
        self.Espacios()
        print('Nombre:', EnCreacion.nombre)
        print('Estados:')
        for estado in EnCreacion.estados:
            print(estado.estado.ljust(10, ' '))
        print('Alfabeto: ', EnCreacion.alfabeto)
        print('Simbolos:', EnCreacion.simbolos)
        print('Estado Inicial:', EnCreacion.inicial)
        print('Estado de aceptacion:', EnCreacion.aceptacion)
        print('Transiciones:')
        for estado in EnCreacion.estados:
            for transicion in estado.transiciones:
                print(str(estado.estado) + ',' + str(transicion.simboloLee) + ',' + str(transicion.simboloExtrae) + ';'
                      + str(transicion.destino) + ',' + str(transicion.simboloInserta))