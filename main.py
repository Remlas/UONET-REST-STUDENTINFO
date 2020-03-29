from vulcan import Vulcan
import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = request.get_json()

    certyfikat = Vulcan.zarejestruj(data['token'], data['symbol'], data['pin'])

    klient = Vulcan(certyfikat)

    x=-1

    osoby = klient.uczniowie()
    osoba = klient.uczniowie()[0]
    if (len(osoby) > 1):
        for przypadek in osoby:
            x = x+1
            if ("SP" not in przypadek.szkola.skrot and "GM" not in przypadek.szkola.skrot and "ZKP" not in przypadek.szkola.skrot and "ZSO10" not in przypadek.szkola.skrot and przypadek.klasa.kod is not None):
                osoba = klient.uczniowie()[x]
    else:
        osoba = klient.uczniowie()[0]

    return {
        "id": osoba.id,
        "imie": osoba.imie,
        "drugie_imie": osoba.drugie_imie,
        "nazwisko": osoba.nazwisko,
        "plec": osoba.plec.name,

        "klasa_id": osoba.klasa.id,
        "klasa_kod": osoba.klasa.kod,

        "szkola_id": osoba.szkola.id,
        "szkola_nazwa": osoba.szkola.nazwa,
        "szkola_skrot": osoba.szkola.skrot
    }

#    return json.dumps(assoc_table, ensure_ascii=False)
