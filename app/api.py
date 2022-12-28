import sys
from flask import Flask, request, jsonify
sys.path.append(r'/Users/wiktoriagirzelska/Desktop/studia/testowanie/lab-2-tworzenie-konta-viensvivre/app')
from Konto import Konto
from RejestrKont import RejestrKont

app = Flask(__name__)
@app.route("/")
def home():
    return "hello world"

@app.route("/konta")
def konta():
    return "Konta"

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.szukaj_po_peselu(dane["pesel"]) == None:
        konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
        RejestrKont.dodaj_konto(konto)
        return jsonify("Konto zostało stworzone"), 200
    else:
        return jsonify("Ten pesel juz istnieje"), 400


@app.route("/konta/ile_kont", methods=['GET'])

def ile_kont():
    return jsonify(RejestrKont.ilosc_kont()), 200

@app.route("/konta/konto/<pesel>", methods=['GET'])

def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont.szukaj_po_peselu(pesel)
    print(konto)

    if konto != None:
        return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200
    else:
        return jsonify("Konto nie istnieje"), 404

@app.route("/konta/konto/<pesel>", methods=['PUT'])

def zaktualizuj_konto_z_peselem(pesel):
    dane = request.get_json()
    print(f"Request o aktualizację konta z peselem: {pesel} i danymi: {dane}")
    konto = RejestrKont.zaktualizuj_konto_z_peselem(pesel, dane)
    print(konto)
    if konto != None:
        return jsonify("Konto zostało zaktualizowane"), 200
    else:
        return jsonify("Konto nie istnieje"), 404

@app.route("/konta/konto/<pesel>", methods=['DELETE'])

def usun_konto_z_peselem(pesel):
    print(f"Request o usunięcie konta z peselem: {pesel}")
    RejestrKont.usun_konto_z_peselem(pesel)
    return jsonify("Konto zostało usunięte"), 200

if __name__ == '__main__':
    app.run()