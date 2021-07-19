""""""""""" 
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven 
fogadható el a megoldás. 

    Készíts egy olyan Python osztályt, ami számolja a fogadott és elküldött üzenetetek és meg tudjá állapítani, 
    hogy ez mennyibe került nekünk. Hogy milyen műveleteket végzett el a felhasználó az legyen egy listában tárolva (
    például: operations = [1,1,1,2,2,1,1,1,2,2,2,2,1,1]). Az 1-es jelentse azt, hogy fogadott egy db üzenetet, 
    a 2-es pedig azt, hogy küldött egyet. Az osztály neve legyen az, hogy MessageBox. 

Kis segítség:

Tehát az osztályod rendelkezzen belül egy eltárolt listával. Ezt a listát csak az osztály használja, kívülről ne írd 
direktben. A feladat része az is, hogy készíts metódusokat amivel az egyes üzenettípusok küldését szimulálod. Az 
üzenet küldést nem kell megvalósítani, hiszen ezt nem kéri senki, csak a képzeletbeli üzenetek elküldésének tényét és 
sorrendjét kell tudni megmondani. Egy jó példa tesztelésre: 

mb = MessageBox()
mb.send()
mb.send()
mb.receive()
mb.receive()
mb.send()

print(mb.operations())
# [2, 2, 1, 1, 2]

"""""""""
