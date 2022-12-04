import unittest
import requests

class TestKontoApi(unittest.TestCase):
    body = {
        'imie': 'wiki',
        'nazwisko': 'g',
        'pesel': '02282093811'
    }

    url = 'http://localhost:5000'

    def test_1_stworz_konto(self):
        create_response = requests.post(self.url + '/konta/stworz_konto', json=self.body)
        self.assertEqual(create_response.status_code, 201)