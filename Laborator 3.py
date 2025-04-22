import json
import random


def citeste_date(fisier):
    try:
        with open(fisier, 'r') as f:
            date = json.load(f)
        return date
    except FileNotFoundError:
        print(f"Fișierul {fisier} nu a fost găsit.")
        return None
    except json.JSONDecodeError:
        print(f"Fișierul {fisier} nu conține un JSON valid.")
        return None


def calculeaza_rest_optim(rest, bancnote):

    inf = float('inf')
    dp = [inf] * (rest + 1)
    dp[0] = 0
    bancnote_folosite = [0] * (rest + 1)

    bancnote_sortate = sorted(bancnote, key=lambda x: x['valoare'], reverse=True)

    for i in range(1, rest + 1):
        for bancnota in bancnote_sortate:
            valoare = bancnota['valoare']
            stoc = bancnota['stoc']

            if valoare <= i and stoc > 0 and dp[i - valoare] != inf and dp[i - valoare] + 1 < dp[i]:
                dp[i] = dp[i - valoare] + 1
                bancnote_folosite[i] = valoare

    if dp[rest] == inf:
        return None

    solutie = []
    suma_ramasa = rest

    while suma_ramasa > 0:
        bancnota_folosita = bancnote_folosite[suma_ramasa]
        solutie.append(bancnota_folosita)
        suma_ramasa -= bancnota_folosita

    numarare_bancnote = {}
    for b in solutie:
        if b not in numarare_bancnote:
            numarare_bancnote[b] = 0
        numarare_bancnote[b] += 1

    for valoare, cantitate in numarare_bancnote.items():
        gasit = False
        for bancnota in bancnote:
            if bancnota['valoare'] == valoare:
                if bancnota['stoc'] < cantitate:
                    return None
                gasit = True
                break
        if not gasit:
            return None

    return solutie


def actualizeaza_stoc(bancnote, bancnote_folosite):
    numarare = {}
    for b in bancnote_folosite:
        if b not in numarare:
            numarare[b] = 0
        numarare[b] += 1

    for valoare, cantitate in numarare.items():
        for bancnota in bancnote:
            if bancnota['valoare'] == valoare:
                bancnota['stoc'] -= cantitate
                break


def simuleaza_casa_de_marcat():
    date = {
        "bancnote": [
            {"valoare": 50, "stoc": 20},
            {"valoare": 20, "stoc": 30},
            {"valoare": 10, "stoc": 40},
            {"valoare": 5, "stoc": 50},
            {"valoare": 1, "stoc": 100}
        ],
        "produse": [
            {"nume": "Lapte", "pret": 7},
            {"nume": "Paine", "pret": 3},
            {"nume": "Ciocolata", "pret": 5},
            {"nume": "Apa", "pret": 2},
            {"nume": "Cafea", "pret": 9}
        ]
    }


    bancnote = date["bancnote"]
    produse = date["produse"]

    nr_client = 1
    while True:
        produs = random.choice(produse)

        suma_platita = produs["pret"] + random.randint(1, 20)

        rest_de_dat = suma_platita - produs["pret"]

        print(f"\nClient {nr_client}:")
        print(f"Produs cumpărat: {produs['nume']}")
        print(f"Preț: {produs['pret']} lei")
        print(f"Suma plătită: {suma_platita} lei")
        print(f"Rest de dat: {rest_de_dat} lei")

        bancnote_rest = calculeaza_rest_optim(rest_de_dat, bancnote)

        if bancnote_rest is None:
            print("\nNu se poate da rest! Simularea se oprește.")
            print("Starea finală a stocului de bancnote:")
            for bancnota in bancnote:
                print(f"Bancnote de {bancnota['valoare']} lei: {bancnota['stoc']} bucăți")
            break

        print("Rest oferit:")
        numarare_bancnote = {}
        for b in bancnote_rest:
            if b not in numarare_bancnote:
                numarare_bancnote[b] = 0
            numarare_bancnote[b] += 1

        for valoare, cantitate in sorted(numarare_bancnote.items(), reverse=True):
            print(f"  {cantitate} x {valoare} lei")

        actualizeaza_stoc(bancnote, bancnote_rest)

        nr_client += 1


if __name__ == "__main__":
    simuleaza_casa_de_marcat()