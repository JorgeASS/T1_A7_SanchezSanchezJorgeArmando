class Calculadora:
    def __init__(self, primerNumero=0, operacion="", segundoNumero=0):
        self.primerNumero = float(primerNumero)
        self.operacion = operacion
        self.segundoNumero = float(segundoNumero)

    def sumar(self):
        return float(self.primerNumero) + float(self.segundoNumero)

    def resta(self):
        return float(self.primerNumero) - float(self.segundoNumero)

    def multiplicar(self):
        return float(self.primerNumero) * float(self.segundoNumero)

    def dividir(self):
        return float(self.primerNumero) / float(self.segundoNumero)

    def indicaResiduo(self):
        return float(self.primerNumero) % float(self.segundoNumero)

    def pos_neg(self):
        if self.segundoNumero > 0:
            return (self.primerNumero * -2) + self.segundoNumero

    def indicarOperacion_Numero(self, num, op):
        self.primerNumero = num
        self.operacion = op
        print(self.primerNumero)
        print(self.operacion)

    def indicarSegundoNumero(self, num):
        self.segundoNumero = num
        print(self.segundoNumero)

    def realizarOperacion(self):
        if (self.operacion == "+"):
            return self.sumar()
        if (self.operacion == "-"):
            return self.resta()
        if (self.operacion == "*"):
            return self.multiplicar()
        if (self.operacion == "/"):
            if self.primerNumero != "0" and self.segundoNumero != "0":
                return self.dividir()
            else:
                return "No es posible dividir entre 0"
        if self.operacion == "%":
            return self.indicaResiduo()
        if self.operacion == "=/-":
            return self.pos_neg()
