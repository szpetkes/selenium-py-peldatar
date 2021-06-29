"""""""""
 A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
 el a megoldás. Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön 
 be egy tetszőleges weblapot az Internetről. Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt. A 
 lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás. Feladatot, hogy kezed le ezt a hibát és írj ki valami 
 emberileg olvasható üzenetet. Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor 
 hívásnál lekezeli a nemlétező elem tipusú hibát. A megoldáshoz használj python try except struktúrát. "" """


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

element_id = input('Kérem adja a keresendő ID t: ')
print('Keresem az oldalon a következő ID-t:', element_id)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("https://www.starwars.com/")

try:
    hiba = driver.find_element_by_id(element_id)

except NoSuchElementException:
    print('Nem létezik ilyen element')
    driver.close()

else:
    print('Az oldalon található', element_id, 'elem')
