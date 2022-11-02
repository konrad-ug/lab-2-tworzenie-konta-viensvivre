import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

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

    def test_urodzeni_po_1960(self):
        szoste_konto = Konto("Jaś", "Fasola", "02254552112", "PROM_XYZ")
        self.assertEqual(szoste_konto.saldo, 50, "Nie uwzględniono kodu rabatowego mimo prawidłowego wieku")

    def test_urodzeni_przed_1960(self):
        siodme_konto = Konto("Adam", "Mickiewicz", "23015849211", "PROM_XXX")
        self.assertEqual(siodme_konto.saldo, 0, "Saldo powinno wynosić zero - osoba urodzona przed 1960")