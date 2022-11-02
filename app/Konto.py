class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = self.sprawdzenie_peselu(pesel)
        self.kod = kod
        self.saldo = self.kod_rabatowy_wiek()

    def sprawdzenie_peselu(self, pesel):
        if len(pesel) == 11:
            return pesel
        else:
            return 'Niepoprawny pesel'

    def rok_urodzenia(self):
        rok = 0
        if len(self.pesel) == 11:
            if int(self.pesel[0]) == 0:
                if int(self.pesel[2] == 0) or int(self.pesel[2] == 1):
                    rok += (1900 + int(self.pesel[1]))
                if int(self.pesel[2] == 2) or int(self.pesel[2] == 3):
                    rok += (2000 + int(self.pesel[1]))
            elif int(self.pesel[0]) > 0:
                if int(self.pesel[2] == 0) or int(self.pesel[2] == 1):
                    rok += (1900 + int(self.pesel[0:2]))
                if int(self.pesel[2] == 2) or int(self.pesel[2] == 3):
                    rok += (2000 + int(self.pesel[0:2]))
        return False

    def czy_po_1960(self):
        if self.rok_urodzenia() != False:
            return self.rok_urodzenia() > 1960
        return "Niepoprawny pesel"

    def kod_rabatowy_wiek(self):
        if self.kod != None and self.czy_po_1960():
            if len(self.kod) == 8:
                poczatek = self.kod[0:5]
                if poczatek == 'PROM_':
                    return 50
        else:
            return 0





