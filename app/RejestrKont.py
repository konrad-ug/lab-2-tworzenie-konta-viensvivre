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