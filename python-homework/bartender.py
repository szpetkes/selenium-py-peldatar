""""" A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven
fogadható el a megoldás.
Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk: sör és kóla. Ha a felhasználó
kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki. Ha a felhasználó 60 feletti, és kólát kér,
akkor közöld vele, hogy a koffein megemelheti a vérnyomását. Ha ismeretlen italt adott meg, akkor írd ki,
hogy csak sört és kólát tudunk adni. Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy
"Parancsoljon,a kólája.") "" """

while True:
    try:
        eletkor = int(input("Hány éves vagy? "))
    except ValueError:
        print("Elnézést nem értettem tisztán! Kérem megismételné?")
        continue
    if eletkor <= 0:
        print("Nem tudom értelmezni!")
        continue
    if eletkor > 120:
        print("Nem tudom értelmezni!")
        continue
    else:
        break

rendeles = input("Sört vagy colát szeretne?: ")
ital1 = 'sör'
ital2 = 'cola'

if eletkor < 18 and rendeles == ital1:
    print("Nem adhatok sört!")
    exit()
else:
    if eletkor >= 60 and rendeles == ital2:
        print('A koffein megemelheti a vérnyomását!')
        exit()
    if eletkor >= 18 and rendeles == ital1 or rendeles == ital2:
        print("Parancsoljon, itt a rendelése!")
    else:
        print("Elnézést! Csak sört vagy colát tudunk adni!")
