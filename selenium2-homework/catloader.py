"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt. Mentsd le az első 20 macskás képet az 
oldalról. A fájlokat egy külön cats könyvtárba mentsd le. A fájlneve legyen a következő {sorszam}_{cat_id} ahol a 
sorszám alatt azt értjük, hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad. A {} 
jelek ne legyenek benne a fájlnévben. 
A megoldást egy catloader.py nevű fileban kell beadnod.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://gentle-bay-0e4e13803.azurestaticapps.net/loadmore.html"
driver.get(URL)

time.sleep(3)
load_more_button = driver.find_element_by_tag_name("button")
for _ in range(2):
    load_more_button.click()
    time.sleep(3)
cats = driver.find_elements_by_tag_name("img")

print(cats)

for index, cat in enumerate(cats):
    url_str = cat.get_attribute("src")
    cat_id = cat.find_element_by_xpath("../p").text.replace("Cat id: ", "")
    cat_file_name = f"cats/{index}_{cat_id}"
    r = requests.get(url_str)
    if r.status_code == 200:
        with open(cat_file_name, 'wb') as f:
            f.write(r.content)

print()
print(len(cats))

"""""
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/loadmore.html")
load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
oldal = 3

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
