while True:
    try:
        kor = int(input("Hány éves vagy? "))
    except ValueError:
        print("Elnézést nem értettem tisztán! Kérem megismételné?")
        continue
    if kor <= 0:
        print("Nem tudom értelmezni!")
        continue
    if kor >120:
        print("Nem tudom értelmezni!")
        continue
    else:
        break

rendelés = input("Sört vagy colát kér?: ")
ital1 = 'sör'
ital2 = 'cola'

if kor < 18 and rendelés == ital1:
    print("Nem adhatok sört!")
    exit()
else:
    if kor >= 60 and rendelés == ital2:
        print('A koffein megemelheti a vérnyomását!')
        exit()
    if kor >= 18 and rendelés == ital1 or rendelés == ital2:
        print("Parancsoljon, itt a rendelése!")
    else:
        print("Sorry! Csak sört vagy colát tudunk adni!")