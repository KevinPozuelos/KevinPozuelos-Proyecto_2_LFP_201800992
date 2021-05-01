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

    def GenerarReporte(self):
        file = open('Carga/automataPila.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        file.write(self.aceptacion + " [shape = doublecircle];" + os.linesep)
        file.write('"Inicio" [shape = plaintext];' + os.linesep)
        file.write('"Inicio" -> ' + self.inicial + os.linesep)
        for est in self.estados:
            for trans in est.transiciones:
                transicion = str(trans.simboloLee) + ',' + str(trans.simboloExtrae) + ';' + str(trans.simboloInserta)
                file.write(est.estado + ' -> ' + trans.destino + ' [label = "{0}"]'.format(transicion) + os.linesep)
        file.write(os.linesep)
        file.write('tabla[shape=plaintext,fontsize=12, label=<')
        file.write('<TABLE BORDER="0">')
        file.write('<TR><TD>Alfabeto: { ' + self.cadenaAlfabeto + ' }</TD></TR>')
        file.write('<TR><TD>Alfabeto de pila: { ' + self.cadenaSimbolos + ' }</TD></TR>')
        file.write('<TR><TD>Estados: { ' + self.cadenaEstados + ' }</TD></TR>')
        file.write('<TR><TD>Estado inicial: { ' + self.inicial + ' }</TD></TR>')
        file.write('<TR><TD>Estado de aceptacion: { ' + self.aceptacion + ' }</TD></TR>')
        file.write('</TABLE>')
        file.write('>];')

        file.write(os.linesep)
        file.write('Titulo [shape=plaintext,fontsize=20, label="Nombre: ' + self.nombre + '"]')

        file.write('}')
        file.close()
        subprocess.call('dot -Tpdf Carga/automataPila.dot -o automataPila.pdf')
        os.system('automataPila.pdf')

    def InsertarAPila(self, simbolo):
        if simbolo != '$' and self.ExisteEnAlfabeto(simbolo):
            self.pila.append(simbolo)
        else:
            '''No se hace nada'''

    def ExtraePila(self, simbolo):
        if simbolo == '$':
            '''No se hace nada'''
            return True
        else:
            if self.pila.pop() == simbolo:
                return True
            else:
                return False

    def ComprobarUltima(self, estado):
        transicionActual = estado.DevolverTransicionCon('$')
        if self.ExtraePila(transicionActual.simboloExtrae):
            self.InsertarAPila(transicionActual.simboloInserta)
            if len(self.pila) == 0 and transicionActual.destino == self.aceptacion:
                return True
            else:
                return False

    def ComprobarUltimaConReporte(self, estado, cadena):
        transicionActual = estado.DevolverTransicionCon('$')
        if self.ExtraePila(transicionActual.simboloExtrae):
            self.InsertarAPila(transicionActual.simboloInserta)
            self.ReportePorPaso(estado.estado, transicionActual, cadena, '1')
            if len(self.pila) == 0 and transicionActual.destino == self.aceptacion:
                self.ReportePorPaso(transicionActual.destino, '', cadena, '2')
                return True
            else:
                return False

    def ValidarCadena(self, cadena):
        self.pila = []
        tamano = len(cadena)

        iteracion = 0
        nombreEstado = self.inicial
        actual = self.SacarEstado(nombreEstado)
        transicionActual = actual.DevolverTransicionCon('$')
        try:
            self.pila.append(transicionActual.simboloInserta)
            nombreEstado = transicionActual.destino
            actual = self.SacarEstado(nombreEstado)
        except:
            print('Error')
            return False

        for caracter in cadena:
            iteracion += 1
            if tamano == iteracion:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                        if self.ComprobarUltima(actual):
                            print('Cadena Valida'.upper())
                            print()
                            return True
                        else:
                            print('Cadena invalida'.upper())
                            print()
                            return False
                    else:
                        print('Cadena invalida'.upper())
                        print()
                        return False
                except:
                    print('Cadena invalida'.upper())
                    print()
                    return False
            else:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                    else:
                        print('Cadena invalida'.upper())
                        print()
                        return False
                except:
                    print('Cadena invalida, caracter no pertenece al automata')
                    print()
                    return False

    def ImprimirCadena(self, cadena):
        self.pila = []
        tamano = len(cadena)

        iteracion = 0
        nombreEstado = self.inicial
        actual = self.SacarEstado(nombreEstado)
        transicionActual = actual.DevolverTransicionCon('$')
        try:
            self.pila.append(transicionActual.simboloInserta)
            print(nombreEstado + transicionActual.ImprimirTransicion())
            nombreEstado = transicionActual.destino
            actual = self.SacarEstado(nombreEstado)
        except:
            print('Error')
            return False

        for caracter in cadena:
            iteracion += 1
            if tamano == iteracion:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        print(nombreEstado + transicionActual.ImprimirTransicion())
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                        if self.ComprobarUltimaImprimiendo(actual):
                            print()
                            return True
                        else:
                            print('Cadena invalida'.upper())
                            print()
                            return False
                    else:
                        print('Cadena invalida'.upper())
                        print()
                        return False
                except:
                    print('Cadena invalida'.upper())
                    print()
                    return False
            else:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        print(nombreEstado + transicionActual.ImprimirTransicion())
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                    else:
                        print('Cadena invalida'.upper())
                        print()
                        return False
                except:
                    print('Cadena invalida, caracter no pertenece al automata')
                    print()
                    return False

    def ComprobarUltimaImprimiendo(self, estado):
        transicionActual = estado.DevolverTransicionCon('$')
        if self.ExtraePila(transicionActual.simboloExtrae):
            self.InsertarAPila(transicionActual.simboloInserta)
            print(estado.estado + transicionActual.ImprimirTransicion())
            if len(self.pila) == 0 and transicionActual.destino == self.aceptacion:
                return True
            else:
                return False

    def ValidarCadenaImprimiendoRuta(self, cadena):
        self.pila = []
        tamano = len(cadena)

        iteracion = 0
        nombreEstado = self.inicial
        actual = self.SacarEstado(nombreEstado)
        transicionActual = actual.DevolverTransicionCon('$')
        try:
            self.pila.append(transicionActual.simboloInserta)
            nombreEstado = transicionActual.destino
            actual = self.SacarEstado(nombreEstado)
        except:
            print('Error')
            return False

        for caracter in cadena:
            iteracion += 1
            if tamano == iteracion:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                        if self.ComprobarUltima(actual):
                            print('Cadena Valida, la ruta de verificacion es:'.upper())
                            self.ImprimirCadena(cadena)
                            print()
                            return True
                        else:
                            print('Cadena invalida'.upper())
                            print()
                            return False
                    else:
                        print('Cadena invalida'.upper())
                        print()
                        return False
                except:
                    print('Cadena invalida'.upper())
                    print()
                    return False
            else:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                    else:
                        print('Cadena invalida'.upper())
                        print()
                        return False
                except:
                    print('Cadena invalida, caracter no pertenece al automata')
                    print()
                    return False

    def CadenaDePila(self):
        cadena = ''
        for caracter in self.pila:
            cadena += caracter
        return cadena

    def TerminarReporteUnaPasada(self, file, iteracion, cadena):
        file.write(
            '<TR><TD>' + str(iteracion + 1) + '</TD><TD>' + self.CadenaDePila() +
            '</TD><TD>' + cadena + '</TD><TD>Invalida</TD></TR>')
        file.write('</TABLE>')
        file.write('>];')
        file.write('}')
        file.close()
        subprocess.call('dot -Tpdf Carga/ValidacionEnUnaPasada.dot -o validacion.pdf')
        os.system('validacion.pdf')

    def ValidarCadenaConReporte(self, cadena):
        self.pila = []
        file = open('Carga/ValidacionEnUnaPasada.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        file.write('tabla[shape=plaintext,fontsize=12, label=<')
        file.write('<TABLE BORDER="1">')
        file.write('<TR><TD>Iteracion</TD><TD>Pila</TD><TD>Entrada</TD><TD>Transicion</TD></TR>')
        tamano = len(cadena)

        iteracion = 0
        nombreEstado = self.inicial
        actual = self.SacarEstado(nombreEstado)
        transicionActual = actual.DevolverTransicionCon('$')
        try:
            self.pila.append(transicionActual.simboloInserta)
            file.write(
                '<TR><TD>0</TD><TD>' + self.CadenaDePila() + '</TD><TD></TD><TD>' + nombreEstado + transicionActual.ImprimirTransicion() + '</TD></TR>')
            nombreEstado = transicionActual.destino
            actual = self.SacarEstado(nombreEstado)
        except:
            print('Error')
            return False

        for caracter in cadena:
            iteracion += 1
            if tamano == iteracion:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        file.write(
                            '<TR><TD>' + str(iteracion) + '</TD><TD>' + self.CadenaDePila() + '</TD><TD>' +
                            cadena[:iteracion] + '</TD><TD>' + nombreEstado + transicionActual.ImprimirTransicion()
                            + '</TD></TR>')
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                        if self.ComprobarUltima(actual):
                            transicionActual = actual.DevolverTransicionCon('$')
                            file.write(
                                '<TR><TD>' + str(iteracion + 1) + '</TD><TD>' + self.CadenaDePila() + '</TD><TD>' +
                                cadena + '</TD><TD>' + nombreEstado + transicionActual.ImprimirTransicion()
                                + '</TD></TR>')
                            file.write('</TABLE>')
                            file.write('>];')
                            file.write('}')
                            file.close()
                            subprocess.call('dot -Tpdf Carga/ValidacionEnUnaPasada.dot -o validacion.pdf')
                            os.system('validacion.pdf')
                            print()
                            return True
                        else:
                            print('Cadena invalida'.upper())
                            self.TerminarReporteUnaPasada(file, iteracion, cadena=cadena[:iteracion])
                            return False
                    else:
                        print('Cadena invalida'.upper())
                        self.TerminarReporteUnaPasada(file, iteracion, cadena=cadena[:iteracion])
                        print()
                        return False
                except:
                    print('Cadena invalida'.upper())
                    self.TerminarReporteUnaPasada(file, iteracion, cadena=cadena[:iteracion])
                    print()
                    return False
            else:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        file.write(
                            '<TR><TD>' + str(iteracion) + '</TD><TD>' + self.CadenaDePila() + '</TD><TD>' +
                            cadena[:iteracion] + '</TD><TD>' + nombreEstado + transicionActual.ImprimirTransicion()
                            + '</TD></TR>')
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                    else:
                        print('Cadena invalida'.upper())
                        self.TerminarReporteUnaPasada(file, iteracion, cadena=cadena[:iteracion])
                        print()
                        return False
                except:
                    print('Cadena invalida, caracter no pertenece al automata')
                    self.TerminarReporteUnaPasada(file, iteracion, cadena=cadena[:iteracion])
                    print()
                    return False

    def ReportePorPaso(self, estado, tran, cadena, numero):
        file = open('Carga/paso.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        file.write(self.aceptacion + " [shape = doublecircle];" + os.linesep)
        if numero == '1':
            '''En proceso'''
            file.write(estado + " [shape = circle, style = filled, fillcolor = yellow];" + os.linesep)
        elif numero == '2':
            file.write('Titulo [shape=plaintext,fontsize=20, label="Cadena Valida"]')
            file.write(self.aceptacion + " [shape = doublecircle, style = filled, fillcolor = yellow];" + os.linesep)
        elif numero == '3':
            file.write('Titulo [shape=plaintext,fontsize=20, label="Cadena invalida"]')
            file.write(estado + " [shape = circle, style = filled, fillcolor = yellow];" + os.linesep)
        else:
            '''naa'''

        file.write('"Inicio" [shape = plaintext];' + os.linesep)
        file.write('"Inicio" -> ' + self.inicial + os.linesep)
        for est in self.estados:
            for trans in est.transiciones:
                transicion = str(trans.simboloLee) + ',' + str(trans.simboloExtrae) + ';' + str(trans.simboloInserta)
                if tran == trans:
                    file.write(est.estado + ' -> ' + trans.destino + ' [label = "{0}", color = red]'.format(transicion) + os.linesep)
                else:
                    file.write(est.estado + ' -> ' + trans.destino + ' [label = "{0}"]'.format(transicion) + os.linesep)
        file.write(os.linesep)
        file.write('tabla[shape=plaintext,fontsize=12, label=<')
        file.write('<TABLE BORDER="1">')
        file.write('<TR><TD>Pila: { ' + self.CadenaDePila() + ' }</TD></TR>')
        file.write('<TR><TD>Entrada: { ' + cadena + ' }</TD></TR>')
        file.write('</TABLE>')
        file.write('>];')



        file.write(os.linesep)

        file.write('}')
        file.close()
        subprocess.call('dot -Tpng Carga/paso.dot -o paso.png')
        os.system('paso.png')
        time.sleep(3)

    def ValidarCadenaMostrandoPasos(self, cadena):
        self.pila = []
        tamano = len(cadena)

        iteracion = 0
        nombreEstado = self.inicial
        actual = self.SacarEstado(nombreEstado)
        transicionActual = actual.DevolverTransicionCon('$')
        try:
            self.pila.append(transicionActual.simboloInserta)
            self.ReportePorPaso(nombreEstado, transicionActual, '', '1')
            nombreEstado = transicionActual.destino
            actual = self.SacarEstado(nombreEstado)
        except:
            print('Error')
            return False

        for caracter in cadena:
            iteracion += 1
            if tamano == iteracion:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        self.ReportePorPaso(nombreEstado, transicionActual, cadena[:iteracion], '1')
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                        if self.ComprobarUltimaConReporte(actual, cadena):

                            print()
                            return True
                        else:
                            self.ReportePorPaso(nombreEstado, transicionActual, cadena[:iteracion], '3')
                            print()
                            return False
                    else:
                        self.ReportePorPaso(nombreEstado, transicionActual, cadena[:iteracion], '3')
                        print()
                        return False
                except:
                    self.ReportePorPaso(nombreEstado, transicionActual, cadena[:iteracion], '3')
                    print()
                    return False
            else:
                transicionActual = actual.DevolverTransicionCon(caracter)
                try:
                    if self.ExtraePila(transicionActual.simboloExtrae):
                        self.InsertarAPila(transicionActual.simboloInserta)
                        self.ReportePorPaso(nombreEstado, transicionActual, cadena[:iteracion], '1')
                        nombreEstado = transicionActual.destino
                        actual = self.SacarEstado(nombreEstado)
                    else:
                        self.ReportePorPaso(nombreEstado, transicionActual, cadena[:iteracion], '3')
                        print()
                        return False
                except:
                    self.ReportePorPaso(nombreEstado, transicionActual, cadena[:iteracion], '3')
                    print()
                    return False

