class KontoFirmowe:
    def __init__(self, nazwa, NIP):
        self.nazwa = nazwa
        if len(NIP) != 10:
            self.NIP = "Niepoprawny NIP"
        else:
            self.NIP = NIP
        self.saldo = 0
        self.historia = []

    def przelew_ekspresowy(self, przelew):
        if self.saldo >= przelew:
            self.saldo -= przelew
            self.saldo -= 5
            self.historia.append(-przelew)
            self.historia.append(-5)

    def zaciagnij_kredyt(self, kredyt):
        if (self.saldo >= 2 * kredyt and -1775 in self.historia):
            self.saldo += kredyt
            return True
        else:
            return False