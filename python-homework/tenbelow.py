"""''
Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek,
mint tíz. Írja ki ezek után a beolvasott számok összegét!
''"""

szam = 0

lista = []

print('FIGYELEM: 10-nél nagyobb szám esetén a program kilép!')

while True:

    szam = int(input('Kérek egy 10-nél kisebb számot: '))
    if szam < 10:
        lista.append(szam)
    else:
        break

print(f'A 10-nél kisebb számok összege: {sum(lista)}')
