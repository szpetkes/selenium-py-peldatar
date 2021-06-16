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
