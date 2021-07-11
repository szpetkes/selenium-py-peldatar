"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt. Mentsd le az első 20 macskás képet az 
oldalról. A fájlokat egy külön cats könyvtárba mentsd le. A fájlneve legyen a következő {sorszam}_{cat_id} ahol a 
sorszám alatt azt értjük, hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad. A {} 
jelek ne legyenek benne a fájlnévben. 
A megoldást egy catloader.py nevű fileban kell beadnod.
"""""
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/loadmore.html")
load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
oldal = 5

local_file = 'c:\\cats'
cat_list = []


def image_load(o):
    for i in range(int(o) - 1):
        load_more.click()


def image_data():
    images = driver.find_elements_by_xpath("//div[@class ='image']")
    time.sleep(4)
    i = 0

    for j in images:
        data_row = {'sorszam': i + 1}
        cat_id = j.find_element_by_tag_name("p").text
        cat_id = cat_id.replace("Cat id: ", "")
        data_row['cat_id'] = cat_id
        with open(f"{local_file}\\{data_row['sorszam']}_{data_row['cat_id']}.jpg", "w") as cat_log:
            cat_log.write(j.find_element_by_tag_name("img").get_attribute("src"))
        cat_list.append(data_row)
        i += 1


driver.quit()
