
meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []

print("Procesare comenzi:")
while studenti and comenzi and tavi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tava = tavi.pop()

    print(f"{student} a comandat {comanda}.")

    istoric_comenzi.append(comanda)
    meniu.remove(comanda)

print("\nComenzi procesate si salvate in istoric.")

print("\nInventar:")
from collections import Counter

contor_comenzi = Counter(istoric_comenzi)

for produs, count in contor_comenzi.items():
    print(f"S-au comandat {count} {produs}")

print(f"Mai sunt {len(tavi)} tavi.")

for produs in ["ceafa", "papanasi", "guias"]:
    disponibil = produs in meniu
    print(f"Mai este {produs}: {disponibil}.")

bani_incasati = sum(dict(preturi)[produs] for produs in istoric_comenzi)
print(f"\nCantina a incasat: {bani_incasati} lei.")

produse_ieftine = [produs for produs in preturi if produs[1] <= 7]
print("Produse care costa cel mult 7 lei:", produse_ieftine)
