class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = self.sprawdzenie_peselu(pesel)
        self.kod = kod
        self.saldo = self.kod_rabatowy_wiek()
        self.historia = []

    def przelew_wychodzacy(self, przelew):
        if self.saldo >= przelew:
            self.saldo -= przelew
            self.historia.append(-przelew)

    def przelew_przychodzacy(self, przelew):
        self.saldo += przelew
        self.historia.append(przelew)

    def przelew_ekspresowy(self, przelew):
        if self.saldo >= przelew:
            self.saldo -= przelew
            self.saldo -= 1
            self.historia.append(-przelew)
            self.historia.append(-1)

    def sprawdzenie_peselu(self, pesel):
        if len(pesel) == 11:
            return pesel
        else:
            return 'Niepoprawny pesel'

    def rok_urodzenia(self):
        rok = 0
        if len(self.pesel) == 11:
            if int(self.pesel[0]) == 0:
                if int(self.pesel[2]) == 0 or int(self.pesel[2]) == 1:
                    rok += (1900 + int(self.pesel[1]))

                    return rok
                elif int(self.pesel[2]) == 2 or int(self.pesel[2]) == 3:
                    rok += (2000 + int(self.pesel[1]))
                    return rok
            elif int(self.pesel[0]) > 0:
                if int(self.pesel[2]) == 0 or int(self.pesel[2]) == 1:
                    rok = (1900 + int(self.pesel[0:2]))
                    return rok
                if int(self.pesel[2]) == 2 or int(self.pesel[2]) == 3:
                    rok += (2000 + int(self.pesel[1]))
                    return rok

    def czy_po_1960(self):
        if self.rok_urodzenia() > 1960:
            return 1
        else:
            return 0

    def kod_rabatowy_wiek(self):
        if self.kod != None and self.czy_po_1960() == 1:

                    if rok<1960:
                        return False
                    else:
                        return True
                if int(self.pesel[2] == 2) or int(self.pesel[2] == 3):
                    rok += (2000 + int(self.pesel[1]))
                    return True
            elif int(self.pesel[0]) > 0:
                if int(self.pesel[2] == 0) or int(self.pesel[2] == 1):
                    rok += (1900 + int(self.pesel[0:2]))
                    if rok<1960:
                        return False
                    else:
                        return True
                if int(self.pesel[2] == 2) or int(self.pesel[2] == 3):
                    rok += (2000 + int(self.pesel[0:2]))
                    return True
            else:
                return False
        else:
            return False

    def czy_po_1960(self):
        if self.rok_urodzenia() != False:
            return True
        return False

    def kod_rabatowy_wiek(self):
        if self.kod != None and self.czy_po_1960() == True:

            if len(self.kod) == 8:
                poczatek = self.kod[0:5]
                if poczatek == 'PROM_':
                    return 50
            return 0
        else:
            return 0

    def warunki_kredytu(self, kredyt):
        if (self.historia[-1] > 0 and self.historia[-2] > 0 and self.historia[-3] > 0 and sum(self.historia[-5:]) > kredyt):
            return True
        else:
            return False

    def zaciagnij_kredyt(self, kredyt):
        if len(self.historia) < 5:
            return False
        else:
            if self.warunki_kredytu(kredyt):
                self.saldo += kredyt
                return True
            return False





