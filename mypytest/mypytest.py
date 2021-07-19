""""""""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
el a megoldás. 

    Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. 
    Válassz ki egy előzőleg megoldott seleniumos példát és írd át pytest-es formára. Érdemes olyat választani, 
    ahol valamit leelenőrzöl, hogy el tudjon esetleg a teszt bukni. Találj ki egy másik tesztet ugyan arra a html 
    oldalra és készíts még egy teszt metódust. 

További segítség

Vegyük például az alábbi selenium tesztet. A file amiben ez a kód le van írva: mywebshop.py

driver.get("https://react-card-2a6c5.web.app/")
time.sleep(2)

# buttons = driver.find_elements_by_xpath('//*[@class="shelf-item__buy-btn"]')
buttons = driver.find_elements_by_class_name("shelf-item__buy-btn")

for button in buttons:
    button.click()
    driver.find_element_by_class_name("float-cart__close-btn").click()
    time.sleep(0.35)

driver.find_element_by_class_name("bag").click()
time.sleep(0.5)
result_text = driver.find_element_by_class_name("sub-price__val").text
assert result_text == "$ 440.00"

Hozzuk Pytest formára.

    Első körben kötelező jelezni a Pytestnek, hogy ez a file teszteket tartalmaz mywebshop.py -> test_mywebshop.py 
    vagy mywebshop.py -> mywebshop_test.py Aztán az is fontos, hogy a benne lévő tesztek test_xyz vagy xyz_test nevű 
    függvényekben legyenek. 

def test_webshop():
    driver.get("https://react-card-2a6c5.web.app/")
    time.sleep(2)

    # buttons = driver.find_elements_by_xpath('//*[@class="shelf-item__buy-btn"]')
    buttons = driver.find_elements_by_class_name("shelf-item__buy-btn")

    for button in buttons:
        button.click()
        driver.find_element_by_class_name("float-cart__close-btn").click()
        time.sleep(0.35)

    driver.find_element_by_class_name("bag").click()
    time.sleep(0.5)
    result_text = driver.find_element_by_class_name("sub-price__val").text
    assert result_text == "$ 440.00"

    Pyteszt formátumban minden metódus egy teszt eset
    Egy python modul tartalmazhat (és tipikusan tartalmaz is) több teszt esetet, tehát tekintheted test suitnak

Bónusz feladat

El lehet ugyan ezeket a teszteket készíteni Objektum Orientáltan is. Próbáld meg őket egy teszt osztályba (class) 
foglalni. Ez az érdekes cikket meg tudod nézni, ha további információ kell: 
https://www.geeksforgeeks.org/object-oriented-testing-in-python/ 

    A megoldást egy mypytest.py nevű fileban kell beadnod. Lehetőleg külön mappában, hiszen ez egy teljes projek.

"""""""""
