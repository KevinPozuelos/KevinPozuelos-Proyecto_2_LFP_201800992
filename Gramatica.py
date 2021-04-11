from NoTerminal import *
import os
import subprocess

class Gramatica(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.terminales = []
        self.cadenaterminales = ''
        self.noterminales = []
        self.cadenanotermianles = ''
        self.inicial = 'inicial'
        self.EsLibreDeContexto = False

    def SacarNoTerminal(self, nombre):
        for noterminal in self.noterminales:
            if noterminal.estado == nombre:
                return noterminal
        return False

    def ExisteEnTerminales(self, parteAlfabeto):
        for parte in self.terminales:
            if parte == parteAlfabeto:
                return True
        return False

    def ExisteNoTermianal(self, nombre):
        for estado in self.noterminales:
            if estado.estado == nombre:
                return True
        return False

    def IngresarAlfabeto(self, parteAlfabeto):
        if self.ExisteNoTermianal(parteAlfabeto):
            print('Este caracter se esta usando como un No Terminal...')
            print('')
        elif self.ExisteEnTerminales(parteAlfabeto):
            print(parteAlfabeto, 'ya es parte de los terminales...')
            print('')
        else:
            self.terminales.append(parteAlfabeto)

    def AgregarEstados(self, nombre):
        if self.ExisteNoTermianal(nombre):
            print('Ya existe un estado con el simbolo', nombre)
            print('')
        else:
            self.noterminales.append(NoTerminal(nombre))
            print('No Terminal', nombre, 'agregado correctamente a la gramatica', self.nombre)
            print('')

    def AgregarTransicion(self, linea):
        separado = linea.split('->')
        produccion = separado[1].split(' ')

        if self.ExisteNoTermianal(separado[0]):
            for analizada in produccion:
                if self.ExisteNoTermianal(analizada) or self.ExisteEnTerminales(analizada):
                    '''Seguimos'''
                else:
                    print('La transicion no se ingreso de forma correcta')
                    return False
            print('Transicion ingresada correctamente')
        else:
            print('La transicion no se ingreso de forma correcta')
            return False
        if len(produccion) == 2:
            if self.ExisteEnTerminales(produccion[0]) and self.ExisteNoTermianal(produccion[1]):
                '''No se hace nada'''
            else:
                self.EsLibreDeContexto = True
        elif len(produccion) == 1 and self.ExisteEnTerminales(produccion[0]):
            '''No se hace nada'''
        else:
            self.EsLibreDeContexto = True

        for noterminal in self.noterminales:
            if noterminal.estado == separado[0]:
                noterminal.transiciones.append(separado[1])
                print('Transicion agregada')

    def AutomataEquivalente(self):
        alfabeto = self.cadenaterminales
        simbolospila = self.cadenaterminales + ',' + self.cadenanotermianles + ',#'
        file = open('Carga/automataPila.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        file.write("rank=same;" + os.linesep)
        file.write("f [shape = doublecircle];" + os.linesep)
        file.write("q [margin = 1];" + os.linesep)
        file.write('"Inicio" [shape = plaintext];' + os.linesep)
        file.write('"Inicio" -> i;' + os.linesep)
        file.write('i -> p [label = "$,$;#"]' + os.linesep)
        file.write('p -> q [label = "$,$;' + self.inicial + '"]' + os.linesep)
        file.write('q -> f [label = "$,#;$"]' + os.linesep)
        for est in self.noterminales:
            for trans in est.transiciones:
                transicion = '"$,' + est.estado + ';' + trans.replace(' ', '') + '"'
                file.write(transicion + ' [shape=none];')
                file.write('q -> ' + transicion + ' [dir = none]' + os.linesep)
                file.write(transicion + '-> q' + os.linesep)
        for terminal in self.terminales:
            transicion = '"' + terminal + ',' + terminal + '; $"'
            file.write(transicion + ' [shape=none];')
            file.write('q -> ' + transicion + ' [dir = none]' + os.linesep)
            file.write(transicion + '-> q' + os.linesep)
        file.write(os.linesep)
        file.write('tabla[shape=plaintext,fontsize=12, label=<')
        file.write('<TABLE BORDER="0">')
        file.write('<TR><TD>Alfabeto: { ' + alfabeto + ' }</TD></TR>')
        file.write('<TR><TD>Alfabeto de pila: { ' + simbolospila + ' }</TD></TR>')
        file.write('<TR><TD>Estados: { i,p,q,f }</TD></TR>')
        file.write('<TR><TD>Estado inicial: { i }</TD></TR>')
        file.write('<TR><TD>Estado de aceptacion: { f }</TD></TR>')
        file.write('</TABLE>')
        file.write('>];')

        file.write(os.linesep)
        file.write('Titulo [shape=plaintext,fontsize=20, label="Nombre: ' + self.nombre + '"]')

        file.write('}')
        file.close()
        subprocess.call('dot -Tpdf Carga/automataPila.dot -o automataPila.pdf')
        os.system('automataPila.pdf')