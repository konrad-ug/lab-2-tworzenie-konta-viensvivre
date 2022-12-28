import unittest
import requests
import sys
sys.path.append(r'/Users/wiktoriagirzelska/Desktop/studia/testowanie/lab-2-tworzenie-konta-viensvivre/app')

class TestKontoApi(unittest.TestCase):
    body = {
        'imie': 'Wiktoria',
        'nazwisko': 'Girzelska',
        'pesel': '02282093811'
    }

    url = 'http://localhost:5000'

    def test_1_stworz_konto(self):
        create_response = requests.post(self.url + '/konta/stworz_konto', json=self.body)
        self.assertEqual(create_response.status_code, 200)
        self.assertEqual(create_response.json(), "Konto zostało stworzone")

    def test_2_szukaj_po_peselu(self):
        create_response2 = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(create_response2.status_code, 200)
        response_body = create_response2.json()
        self.assertEqual(response_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(response_body["imie"], self.body["imie"])
        self.assertEqual(response_body["saldo"], 0)

    def test_3_update_po_peselu(self):
        put_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json=self.data)
        self.assertEqual(put_resp.status_code, 200)
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["imie"], self.data["imie"])
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["pesel"], self.body["pesel"])
        self.assertEqual(resp_body["saldo"], self.data["saldo"])


#unittest.main()