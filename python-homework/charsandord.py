""""" A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven 
fogadható el a megoldás. 
Írj programot, ami kiírja a kisbetűket, és melléjük az ASCII kódjukat! A kiírás több oszlopos legyen, 
és legfeljebb 10 soros. Minta: 
a 97 f 102 .....
b 98 g 103
c 99 h 104
d 100 i 105
e 101 j 106
A megoldashoz használd a beépített ord() es chr() függvényeket.
"""""

x = ord('x')

for i in range(10):
    if i < 26 % 10:
        print(f'{chr(x + i)}', x + i, f'{chr(x + i + 10)}', x + i + 10, f'{chr(x + i + 20)}', x + i + 20)
    else:
        print(f'{chr(x + i)}', x + i, f'{chr(x + i + 10)}', x + i + 10)
