"""''''''
Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg a felhasználó nullát nem ad
be! A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit fordított sorrendben!
A megoldást egy fordito.py nevű file-ban kell beadnod.
''''''"""

numbers = []
while True:
    number = int(input("Írj be egy pozitív egész számot:"))
    if number > 0:
        numbers.append(number)
    else:
        break
numbers.reverse()
print('Bekért számok a beírás sorrendjében:', numbers[::-1])
