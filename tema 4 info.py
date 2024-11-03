import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

print("Bine ai venit la jocul Spanzuratoarea!")
print("Cuvant de ghicit:", " ".join(progres))
print("Ai", incercari_ramase, "incercari ramase.\n")

while incercari_ramase > 0 and "_" in progres:
    litera = input("Introdu o litera: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Te rog introdu o singura litera valida.")
        continue
    if litera in litere_incercate:
        print("Ai incercat deja aceasta litera. Alege alta.")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for i, c in enumerate(cuvant_de_ghicit):
            if c == litera:
                progres[i] = litera
        print("Corect! Litera se afla in cuvant.")
    else:
        incercari_ramase -= 1
        print("Gresit! Litera nu se afla in cuvant.")

    print("Progres:", " ".join(progres))
    print("Incercari ramase:", incercari_ramase)
    print("Litere incercate:", ", ".join(litere_incercate), "\n")

if "_" not in progres:
    print("Felicitari! Ai ghicit cuvantul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvantul era:", cuvant_de_ghicit)
