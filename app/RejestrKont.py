class RejestrKont:

    listaKont = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.listaKont.append(konto)

    @classmethod
    def szukaj_po_peselu(cls, pesel):
        for i in cls.listaKont:
            if i.pesel == pesel:
                return i
        return None

    @classmethod
    def ilosc_kont(cls):
        print(cls.listaKont)
        return len(cls.listaKont)

    @classmethod
    def zaktualizuj_konto_z_peselem(cls, pesel, dane):
        konto = cls.szukaj_po_peselu(pesel)
        if konto != None:
            konto.imie = dane['imie'] if 'imie' in dane else konto.imie
            konto.nazwisko = dane['nazwisko'] if 'nazwisko' in dane else konto.nazwisko
            konto.pesel = dane['pesel'] if 'pesel' in dane else konto.pesel
            konto.saldo = dane['saldo'] if 'saldo' in dane else konto.saldo
        return konto

    @classmethod
    def usun_konto_z_peselem(cls, pesel):
        konto = cls.szukaj_po_peselu(pesel)
        if konto != None:
            cls.listaKont.remove(konto)
        return konto