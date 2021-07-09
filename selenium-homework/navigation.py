"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/general.html oldalt. A feladatod, hogy végiglátogassd az 
összes linket ezen az oldalon. Egy link meglátogatása akkor érvényes, ha a hozzá tartozó a html elemre 
rákattintottál, a megjelent új oldalnak ellenrőizted, hogy eggyezik az urlje az előzőleg használt a tag href-jével és 
sikeresen vissza navigáltál a főoldalra. (A tökéletes megoldás nem tartalmaz sor ismétléseket. Ezt mondjuk függvények 
írásák is elő tudod idézni.) 
""" ""

from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("http://localhost:9999/general.html")

page = "http://localhost:9999/general.html"


def links():
    return driver.find_elements_by_xpath("//a")


v = links()

for link in v:
    k = link.get_attribute('href')
    if page in k:
        link.click()
        print("URL OK", k)
        driver.back()
    else:
        driver.close()

if link.get_attribute():
    print('NOT OK')
