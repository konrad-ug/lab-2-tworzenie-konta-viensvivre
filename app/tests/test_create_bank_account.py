import sys
import unittest
sys.path.append(r'/Users/wiktoriagirzelska/Desktop/studia/testowanie/lab-2-tworzenie-konta-viensvivre/app')
from Konto import Konto
from Konto import KontoFirmowe

class testCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "02561422920")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "02561422920", "Pesel jest za krótki")
        self.assertEqual(pierwsze_konto.kod, None, "Kod rabatowy został podany, a 50zl nie zostało dodane do salda ")

    def test_za_krotki_pesel(self):
        drugie_konto = Konto("Wiktoria", "Girzelska", "0264823")
        self.assertEqual(drugie_konto.pesel, "Niepoprawny pesel", "Za krótki pesel, a nie wyświetla błędu")

    def test_za_dlugi_pesel(self):
        trzecie_konto = Konto("Tomasz", "Kijek", "0264823992030")
        self.assertEqual(trzecie_konto.pesel, "Niepoprawny pesel", "Za długi pesel, a nie wyświetla błędu")

    def test_dobry_kod_rabatowy_saldo(self):
        czwarte_konto = Konto("Jan", "Kowalski", "77128219121", "PROM_XYZ")
        self.assertEqual(czwarte_konto.kod, "PROM_XYZ", "Niepoprawny kod rabatowy")
        self.assertEqual(czwarte_konto.saldo, 50, "Bonus nie został dodany")

    def test_zly_kod_rabatowy_saldo(self):
        piate_konto = Konto("Adam", "Malysz", "77128219121", "PGISWJ")
        self.assertEqual(piate_konto.saldo, 0, "Bonus został dodany, mimo że kod jest nieprawidłowy")

    def test_urodzeni_w_latach_1900_1909(self):
        osme_konto =  Konto("Borys", "Kowalski", "08114887211", "PROM_XUZ")
        self.assertEqual(osme_konto.saldo, 0, "Uwzględniono bonus pomimo złego wieku")

    def test_urodzeni_w_latach_2010_plus(self):
        osme_konto = Konto("Borys", "Kowalski", "12214887211", "PROM_XUZ")
        self.assertEqual(osme_konto.saldo, 50, "Nie uwzględniono kodu rabatowego mimo prawidłowego wieku")

    def test_urodzeni_po_1960(self):
        szoste_konto = Konto("Jaś", "Fasola", "02254552112", "PROM_XYZ")
        self.assertEqual(szoste_konto.saldo, 50, "Nie uwzględniono kodu rabatowego mimo prawidłowego wieku")

    def test_urodzeni_przed_1960(self):
        siodme_konto = Konto("Adam", "Mickiewicz", "43015849211", "PROM_XXXZ")
        self.assertEqual(siodme_konto.saldo, 0, "Uwzględniono bonus pomimo złego wieku")

class TestPrzelewy(unittest.TestCase):

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        konto = Konto("Dariusz", "Januszewski", "02561422920")
        przelew = 200
        konto.saldo = 500
        konto.przelew_wychodzacy(przelew)
        self.assertEqual(konto.saldo, 500 - przelew, "Nie udało się wykonać przelewu")

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        konto = Konto("Dariusz", "Januszewski", "02561422920")
        przelew = 600
        konto.saldo = 500
        konto.przelew_wychodzacy(przelew)
        self.assertEqual(konto.saldo, 500, "Niewystarczające środki a przelew został wykonany")

    def test_przelew_przychodzacy(self):
        konto = Konto("Dariusz", "Januszewski", "02561422920")
        przelew = 300
        konto.saldo = 500
        konto.przelew_przychodzacy(przelew)
        self.assertEqual(konto.saldo, 500 + przelew, "Przelew nie został wykonany")

    def test_kilka_przelewow(self):
        konto = Konto("Dariusz", "Januszewski", "02561422920")
        konto.saldo = 500
        konto.przelew_przychodzacy(300)
        konto.przelew_wychodzacy(400)
        konto.przelew_przychodzacy(500)
        konto.przelew_wychodzacy(250)
        self.assertEqual(konto.saldo, 500+300-400+500-250, "Nie udało się wykonać wszystkich przelewów")

class KontaFirmowe(unittest.TestCase):

    def test_konto_firmowe(self):
        konto1 = KontoFirmowe("Budimex", "2203488202")
        self.assertEqual(konto1.nazwa, "Budimex", "Nazwa nie została zapisana")
        self.assertEqual(konto1.NIP, "2203488202", "NIP nie został zapisany")

    def test_poprawny_NIP(self):
        konto1 = KontoFirmowe("Budimex", "2203202895")
        self.assertEqual(len(konto1.NIP), 10, "Niepoprawna długość NIP")

    def test_niepoprawny_NIP(self):
        konto1 = KontoFirmowe("Budimex", "22895")
        self.assertEqual(konto1.NIP, "Niepoprawny NIP")

class TestPrzelewyEkspresowe(unittest.TestCase):

    def test_ekspresowy_konto_zwykle_udany_przelew(self):
        konto = Konto("Dariusz", "Januszewski", "02561422920")
        konto.saldo = 600
        konto.przelew_ekspresowy(400)
        self.assertEqual(konto.saldo, 600-400-1, "Nie udało się wykonać przelewu")

    def test_ekspresowy_konto_zwykle_nieudany_przelew(self):
        konto = Konto("Dariusz", "Januszewski", "02561422920")
        konto.saldo = 500
        konto.przelew_ekspresowy(600)
        self.assertEqual(konto.saldo, 500, "Przelew wykonany pomimo niewystarczających środków")

    def test_ekspresowy_konto_firmowe_udany_przelew(self):
        konto = KontoFirmowe("Budimex", "2203202895")
        konto.saldo = 650
        konto.przelew_ekspresowy(350)
        self.assertEqual(konto.saldo, 650-350-5, "Nie udało się wykonać przelewu")

    def test_ekspresowy_konto_firmowe_nieudany_przelew(self):
        konto = KontoFirmowe("Budimex", "2203202895")
        konto.saldo = 250
        konto.przelew_ekspresowy(350)
        self.assertEqual(konto.saldo, 250, "Przelew wykonany pomimo niewystarczających środków")

unittest.main()