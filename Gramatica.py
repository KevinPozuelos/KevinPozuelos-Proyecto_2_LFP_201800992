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
