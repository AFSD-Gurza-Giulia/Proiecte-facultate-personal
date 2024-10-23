import string

# Textul copiat de pe Wikiștiri (fără diacritice)
text = """
BUCURESTI, ROMANIA, ACTUALITATE ELENA UDREA A FOST EXTRADATA IN ROMANIA DIN BULGARIA, PE 16 IUNIE 2022, DUPA MAI BINE DE DOUA LUNI DE LA MOMENTUL IN CARE A FOST RETINUTA DE AUTORITATILE BULGARE LA GRANITA CU GRECIA.

DUPA MAI MULTE INFATISARI IN INSTANTELE DIN BULGARIA, JUDECATORII BULGARI AU DECIS CA PUN IN APLICARE MANDATUL EUROPEAN DE ARESTARE EMIS PE NUMELE ELENEI UDREA.

FOSTUL MINISTRU AL DEZVOLTARII A FOST PREDATA AUTORITATILOR ROMANE IN CONDITII SPECIALE, LA VAMA GIURGIU-RUSE. DUPA CE VA AJUNGE LA PENITENCIARUL TARGSOR, ELENA UDREA VA FI SUPUSA UNUI PROGRAM DE CARANTINA DE 21 DE ZILE, PERIOADA IN CARE VA FI SUPUSA UNUI PROGRAM DE EVALUARE.
"""

# Imparte sirul in doua parti egale
mid = len(text) // 2
first_half = text[:mid]
second_half = text[mid:]

# Operatii pe prima parte
# Transforma toate literele in majuscule si elimina spatiile de la inceput si final
first_half = first_half.upper().strip()

# Operatii pe a doua parte
# Elimina toate caracterele de punctuatie inainte de a inversa
second_half = second_half.translate(str.maketrans('', '', string.punctuation))

# Inverseaza ordinea caracterelor
second_half = second_half[::-1]

# Transforma prima litera in majuscula (restul in litere mici)
second_half = second_half.capitalize()

# Combina cele doua parti
result = first_half + second_half

# Afiseaza rezultatul final
print(result)
