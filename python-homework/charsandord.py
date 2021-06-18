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

import string
raw = ''

for i in range(0, len(string.ascii_lowercase)):
    abc = string.ascii_lowercase[i]
    if i > 0 and (i % 3) == 0:
        print(raw + '')
        raw = ''
    raw += '\t' + abc + ' ' + str(ord(abc))
print(abc + '')
