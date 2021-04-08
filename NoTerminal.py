class NoTerminal(object):
    def __init__(self, nombre):
        self.estado = nombre
        self.transiciones = []
        self.consulta = 0

    def DevolverUnaTransicion(self):
        consultaActual = self.consulta
        self.consulta += 1
        if self.consulta > (len(self.transiciones) - 1):
            self.consulta = 0
        return self.transiciones[consultaActual]