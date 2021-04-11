from Transicion import *

class EstadoAP(object):
    def __init__(self, nombre):
        self.estado = nombre
        self.transiciones = []

    def YaTengoEseSimbolo(self, simbolo):
        for transicion in self.transiciones:
            if transicion.simboloLee == simbolo:
                return True
        else:
            return False

    def AgregarTransicion(self, lee, extrae, destino, inserta):
        if self.YaTengoEseSimbolo(lee):
            print('En los automatas de pila un estado no puede llevar a ')
            print('diferentes estados usando el mismo terminal')
            input('Enter para continuar...')
            return False
        else:
            self.transiciones.append(transiciones(lee, extrae, destino, inserta))
            print('Transicion agregada correctamente')
            print('')
            return True

    def TieneTransicionCon(self, simbolo):
        for tran in self.transiciones:
            if tran.simboloLee == simbolo:
                return True
        return False

    def DevolverTransicionCon(self, simbolo):
        if self.TieneTransicionCon(simbolo):
            for tran in self.transiciones:
                if tran.simboloLee == simbolo:
                    return tran
        else:
            return False