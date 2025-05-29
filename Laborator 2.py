import hashlib


# Functia pentru calcularea hash-ului unei parole
def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Hash-ul parolei pe care trebuie sa o gasim
target_hash = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

# Contorul pentru numarul de apeluri recursive
numar_apeluri = 0

# Caracterele pe care le putem folosi
litere_mari = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
litere_mici = "abcdefghijklmnopqrstuvwxyz"
cifre = "0123456789"
caractere_speciale = "!@#$"


def verifica_conditii(parola_candidat):
    """
    Verifica daca parola candidat respecta toate conditiile:
    - exact 1 litera mare
    - exact 1 cifra
    - exact 1 caracter special
    - exact 3 litere mici
    """
    nr_litere_mari = 0
    nr_litere_mici = 0
    nr_cifre = 0
    nr_caractere_speciale = 0

    for caracter in parola_candidat:
        if caracter in litere_mari:
            nr_litere_mari += 1
        elif caracter in litere_mici:
            nr_litere_mici += 1
        elif caracter in cifre:
            nr_cifre += 1
        elif caracter in caractere_speciale:
            nr_caractere_speciale += 1

    # Verifica daca avem exact numarul dorit de fiecare tip de caracter
    return (nr_litere_mari == 1 and nr_litere_mici == 3 and
            nr_cifre == 1 and nr_caractere_speciale == 1)


def backtrack_parola(parola_actuala, pozitie):
    """
    Functia recursiva de backtracking pentru generarea parolelor candidate
    parola_actuala = parola construita pana acum
    pozitie = pozitia curenta in parola (0-5 pentru o parola de 6 caractere)
    """
    global numar_apeluri
    numar_apeluri += 1

    # Cazul de baza: am completat o parola de 6 caractere
    if pozitie == 6:
        # Verifica daca parola respecta conditiile
        if verifica_conditii(parola_actuala):
            # Calculeaza hash-ul parolei candidate
            hash_candidat = get_hash(parola_actuala)
            # Verifica daca hash-ul se potriveste cu cel cautat
            if hash_candidat == target_hash:
                print()
                print("🎉 SUCCES! PAROLA GASITA! 🎉")
                print("-" * 60)
                print(f"🔑 Parola gasita: {parola_actuala}")
                print(f"🔢 Hash verificat: {hash_candidat}")
                print(f"📊 Numar apeluri recursive: {numar_apeluri:,}")
                print("-" * 60)
                return True
        return False

    # Incercam sa adaugam fiecare tip de caracter la pozitia curenta
    toate_caracterele = litere_mari + litere_mici + cifre + caractere_speciale

    for caracter in toate_caracterele:
        # Afisam progresul la fiecare 10000 de apeluri
        if numar_apeluri % 10000 == 0:
            print(f"🔄 Progres: {numar_apeluri:,} incercari... Construim: '{parola_actuala + caracter}'")

        # Adaugam caracterul la parola
        parola_noua = parola_actuala + caracter

        # Apelam recursiv pentru pozitia urmatoare
        if backtrack_parola(parola_noua, pozitie + 1):
            return True  # Am gasit parola, oprim cautarea

    return False


def gaseste_parola():
    """
    Functia principala care porneste procesul de cautare
    """
    print("=" * 60)
    print("🔓 SPARGATOR DE PAROLE - BACKTRACKING 🔓")
    print("=" * 60)
    print("📋 CONDITII PAROLA:")
    print("   • 1 litera mare (A-Z)")
    print("   • 1 cifra (0-9)")
    print("   • 1 caracter special (!@#$)")
    print("   • 3 litere mici (a-z)")
    print("   • Lungime totala: 6 caractere")
    print()
    print("🎯 TARGET HASH:")
    print(f"   {target_hash}")
    print()
    print("🔍 INCEPEM CAUTAREA...")
    print("-" * 60)

    import time
    start_time = time.time()

    # Pornim backtracking-ul cu o parola goala de la pozitia 0
    if not backtrack_parola("", 0):
        print()
        print("❌ REZULTAT: Nu s-a gasit nicio parola!")
        print(f"📊 Apeluri recursive totale: {numar_apeluri:,}")

    end_time = time.time()
    timp_executie = end_time - start_time
    print(f"⏱️  Timp executie: {timp_executie:.2f} secunde")
    print("=" * 60)


# Rulam programul
if __name__ == "__main__":
    gaseste_parola()