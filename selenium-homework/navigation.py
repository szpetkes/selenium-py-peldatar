"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/general.html oldalt. A feladatod, hogy végiglátogassd az 
összes linket ezen az oldalon. Egy link meglátogatása akkor érvényes, ha a hozzá tartozó a html elemre 
rákattintottál, a megjelent új oldalnak ellenrőizted, hogy eggyezik az urlje az előzőleg használt a tag href-jével és 
sikeresen vissza navigáltál a főoldalra. (A tökéletes megoldás nem tartalmaz sor ismétléseket. Ezt mondjuk függvények 
írásával is elő tudod idézni.) 
""" ""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("http://localhost:9999/general.html")

try:
    urls_to_open = []
    urls = driver.find_elements_by_xpath("//*[@href]")

    for i in urls:
        i = i.get_attribute('href')
        urls_to_open.append(i)

    for i in urls_to_open:
        urls_to_open = "'" + i + "'"
        print(urls_to_open, '\n')
        driver.get(i)
        time.sleep(1)
finally:
    driver.close()
