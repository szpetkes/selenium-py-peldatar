"""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.

    Kérjünk be két számot, és írjuk ki a különgségüket. Használd az input() és print() beépített függvényeket.

        A megoldást egy substract.py nevű file-ban kell beadnod.

    Az autód 7 litert fogyaszt országúton és 9-et városban. A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban. Mennyit fogyaszt az autód csak oda? És oda-vissza? Mennyibe kerül a teljes út, ha 350 Ft a benzin? Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel (országúti fogyasztás, városi fogyasztás, országúton megtett út, városban megtett út, benzin ára) dolgozol, hanem a felhasználótól kéred ezeket be. Ahol szükséges, ne feledd konvertálni az értékeket! 
"""""

a =input('Autód városi fogyasztása:')
b =input('Autód országúti fogyasztása:')
c =input('Megtett út városban:')
d =input('Megtett út országúton:')
e =input('Benzin fogyasztási ára:')

fogyasztas_liter = (float((int(c)*int(a))/100)) + (float((int(d)*int(b))/100))
fogyasztas_forint = int(fogyasztas_liter*float(e))

print('Odautazás fogyasztása:', fogyasztas_liter, 'liter')
print('Visszautazás fogyasztása:', float(fogyasztas_liter) * 2 , 'liter')
print('Oda-vissza utazás költsége:', fogyasztas_forint, 'Ft')
