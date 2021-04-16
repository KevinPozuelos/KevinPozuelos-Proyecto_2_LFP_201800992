from Gramatica import *

class ListaGramatica(object):
    def __init__(self):
        self.gramatica = []

    def ExisteGramatica(self, AFD):
        for afd in self.gramatica:
            if afd.nombre == AFD:
                print('Existe una gramatica con ese nombre')
                return True
        return False

    def EstaVacio(self):
        if len(self.gramatica) == 0:
            return True
        else:
            return False

    def EliminarAFD(self, nombre):
        for afd in self.gramatica:
            if afd.nombre == nombre:
                self.gramatica.remove(afd)
                print('Gramatica eliminada')

    def Agregar(self, AFD):
        if not self.ExisteGramatica(AFD.nombre):
            self.gramatica.append(AFD)
        else:
            '''Ya se manda mensaje desde el otro metodo'''

    def MostrarGramaticas(self):
        for afd in self.gramatica:
            print(afd.nombre)


    def CargarGramaticas(self, ruta):
        global EnCreacion
        automatas = open(ruta, 'r')
        noL = 0  # Numero de linea
        for linea in automatas.readlines():
            noL += 1
            linea = linea.replace('\n', '')

            if noL == 1:  # Ingresando titulo al automata
                if not self.ExisteGramatica(linea):
                    EnCreacion = Gramatica(linea)
                    print(EnCreacion.nombre, 'creandose')
                else:
                    self.EliminarAFD(linea)
                    EnCreacion = Gramatica(linea)
                    print(EnCreacion.nombre, 'creandose')
            elif noL == 2:  # Ingresando alfabeto del automata
                contador = 0
                for d in linea.split(';'):
                    print(d)
                    if contador == 0:
                        for alfa in d.split(','):
                            EnCreacion.AgregarEstados(alfa)
                            EnCreacion.cadenanotermianles = d
                    elif contador == 1:
                        for alfa in d.split(','):
                            EnCreacion.IngresarAlfabeto(alfa)
                        EnCreacion.cadenaterminales = d
                    elif contador == 2:
                        EnCreacion.inicial = d
                    contador += 1
            elif linea == '*':
                print(' ')
                if EnCreacion.EsLibreDeContexto:
                    self.gramatica.append(EnCreacion)
                    print('Automata agregado correctamente')
                    self.ImprimirAutomata(EnCreacion)

                else:
                    print('No es una gramatica libre del contexto, no sera agregada')
                noL = 0
            else:
                EnCreacion.AgregarTransicion(linea)
        automatas.close()

    def ImprimirAutomata(self, EnCreacion):

        print('Nombre:', EnCreacion.nombre)
        print('No terminales:', EnCreacion.cadenanotermianles)
        print('Terminales: ', EnCreacion.cadenaterminales)
        print('No terminal inicial:', EnCreacion.inicial)
        print('Producciones:')
        n = 0
        for estado in EnCreacion.noterminales:
            n += 1
            no = 1
            for transicion in estado.transiciones:
                if no == 1:
                    print("producion "+str(n)+': '+estado.estado, '->', transicion)
                else:
                    print("\t"+"\t"+"\t"+"\t"+'|', transicion)
                no += 1

    def DevolverADP(self, nombre):
        for adp in self.gramatica:
            if adp.nombre == nombre:
                return adp
        return False