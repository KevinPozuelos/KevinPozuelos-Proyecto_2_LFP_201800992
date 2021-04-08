class transiciones(object):
    def __init__(self, lee, extrae, destino, inserta):
        self.simboloLee = lee
        self.simboloExtrae = extrae
        self.destino = destino
        self.simboloInserta = inserta

    def Extrae(self):
        return self.simboloExtrae

    def Inserta(self):
        return self.simboloInserta

    def ImprimirTransicion(self):
        trans = ','+self.simboloLee + ',' + self.simboloExtrae + ';' + self.destino + ',' + self.simboloInserta
        return trans
