"""""""""
Adott az alábbi csv tartalom

Name,Email,DoB,Phone
Kiss Péter,peter.kiss@sel.hu,1988-12-12,06361 455899
Nagy Ervin,ervin.nagy@sel.hu,1977-01-01,06361 555555
Bella Eszter, eszter.bella@sel.hu,2003-07-07, 06555 555555
Kis Franciska, franciska.kiss@sel.hu,1999-01-20, 06666 666666

Metsd ezt el egy table_in.csv szöveges állományba. Ezzel fogsz dolgozni.

Készíts egy python programot ami a fenti adatfileból készít egy másik adatfájl-t ami csak az emailcím és név 
oszlopokat tartalmazza. Tehát például: 

Email,Name
peter.kiss@sel.hu,Kiss Péter
ervin.nagy@sel.hu,Nagy Ervin
...

> A megoldást egy `csvszures.py` nevű fileban kell beadnod.
"""""""""
import csv

with open("table_in.csv", encoding="utf-8") as csv_file:
    beolvasott = csv.reader(csv_file, delimiter=',')
    for row in beolvasott:
        print(f'Email: {row[1]} Name: {row[0]} ')


# with open('email_and_name.csv', 'w', encoding="UTF-8") as email_and_name:
