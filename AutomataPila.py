from EstadoAutomataPila import *
import os
import subprocess
import time

class AutomataPila(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.estados = []
        self.cadenaEstados = ''
        self.alfabeto = []
        self.cadenaAlfabeto = ''
        self.simbolos = []
        self.cadenaSimbolos = ''
        self.inicial = 'inicial'
        self.aceptacion = 'aceptacion'
        self.pila = []

    def HacerSimbolos(self):
        self.simbolos = self.alfabeto
        self.simbolos.append('#')

    def SacarEstado(self, nombre):
        for estado in self.estados:
            if estado.estado == nombre:
                return estado
        return False

    def ExisteEnAlfabeto(self, parteAlfabeto):
        for parte in self.alfabeto:
            if parte == parteAlfabeto:
                return True
        return False

    def ExisteEnSimbolos(self, parteAlfabeto):
        for parte in self.simbolos:
            if parte == parteAlfabeto:
                return True
        return False

    def AlfabetoLamda(self, parteAlfabeto):
        if self.ExisteEnSimbolos(parteAlfabeto) or (parteAlfabeto == '$'):
            return True
        return False

    def ExisteEstado(self, nombre):
        for estado in self.estados:
            if estado.estado == nombre:
                return True
        return False

    def IngresarAlfabeto(self, parteAlfabeto):
        if self.ExisteEstado(parteAlfabeto):
            print('Este caracter se esta usando como un estado...')
            print('')
        elif self.ExisteEnAlfabeto(parteAlfabeto):
            print(parteAlfabeto, 'ya es parte del alfabeto...')
            print('')
        else:
            self.alfabeto.append(parteAlfabeto)

    def IngresarSimbolos(self, simbolo):
        if self.ExisteEstado(simbolo):
            print('Este caracter se esta usando como un estado...')
            print('')
        elif self.ExisteEnSimbolos(simbolo):
            print(simbolo, 'ya es parte de los simmbolos...')
            print('')
        else:
            self.simbolos.append(simbolo)

    def AgregarEstados(self, nombre):
        if self.ExisteEstado(nombre):
            print('Ya existe un estado con el simbolo', nombre)
            print('')
        else:
            self.estados.append(EstadoAP(nombre))
            print('Estado', nombre, 'agregado correctamente al automata', self.nombre)
            print('')

    def AgregarTransicion(self, cadena):
        try:
            separado = cadena.split(';')
            Parte1 = separado[0].split(',')
            Parte2 = separado[1].split(',')
            origen = Parte1[0]
            lee = Parte1[1]
            extrae = Parte1[2]
            destino = Parte2[0]
            inserta = Parte2[1]

            if (origen != ' ') and (lee != ' ') and (extrae != ' ') and (destino != ' ') and (inserta != ' '):
                print('Transicion ingresada correctamente')
            else:
                print('La transicion no se ingreso de forma correcta')
                return False
        except:
            print('La transicion no se agrego de forma correcta')
            return False

        if self.ExisteEstado(origen) and self.AlfabetoLamda(lee) and self.AlfabetoLamda(extrae) and self.ExisteEstado(
                destino) and self.AlfabetoLamda(inserta):

            for estado in self.estados:
                if estado.estado == origen:
                    return estado.AgregarTransicion(lee, extrae, destino, inserta)

        else:
            print('')
            print(
                'No es posible agregar esta transicion, algun estado o el simbolo no estan registrados en el automata')
            return False