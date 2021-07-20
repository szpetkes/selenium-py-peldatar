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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.get("https://react-card-2a6c5.web.app/")
    return driver


def test_first_testcase(browser):
    yes_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'yes')))
    yes_element.click()
    browser.find_element_by_id("buttoncheck").click()
    p = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="container"]/p')))
    print(p.text)


def test_second_testcase(browser):
    browser.get("https://google.com")
    time.sleep(2)
    assert True


driver.quit()

