"""Szökőév? - Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik,
nem szökőév minden századik, mégis az minden 400-adik. (2000-ben ezért volt szökőév.) A függvény visszatérési értéke
legyen logikai típusú! Tipp( % maradekos osztas operátor) - Írj programot, amelyik a felhasználótól évszámokat kér,
és mindegyikre kiírja, hogy szökőév-e! Használd az előbb megírt függvényt! Például: ? 2005 Nem szökőév. ? 2000
Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév. """


def ev(megadott_ev: int) -> bool:
    szokoev = False

    if (megadott_ev % 4) == 0:
        if (megadott_ev % 100) == 0:
            if (megadott_ev % 400) == 0:
                szokoev = True
            else:
                szokoev = False
        else:
            szokoev = True
    return szokoev


def main():
    while True:
        megadott_ev = int(input('Adjon meg egy évszámot (kilépés nullával): '))

        if megadott_ev == 0:
            print('Viszlát!')
            break
        if ev(megadott_ev):
            print(f'{megadott_ev} Az év IGEN szökőév')
        else:
            print(f'{megadott_ev} Az év NEM szökőév')


if __name__ == "__main__":
    main()
