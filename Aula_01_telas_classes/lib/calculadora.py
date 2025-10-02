class Calculadora:

    def __init__(self):
        self._numero1 = 0
        self._numero2 = 0

    @property
    def numero1(self):
        return self._numero1
    @property
    def numero2(self):
        return self._numero2
    @numero1.setter
    def numero1(self, value):
        self._numero1 = value
    @numero2.setter
    def numero2(self, value):
        self._numero2 = value

    def somar(self, numero1, numero2):
        return numero1 + numero2
