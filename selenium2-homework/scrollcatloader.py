"""""""""" 
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar 
alkalmazást. A program töltse be a példatárból az http://localhost:9999/scrolltoload.html oldalt. Mentsd le az első 
20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le. A fájlneve legyen a következő {
sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit 
szolgáltató ad. A {} jelek ne legyenek benne a fájlnévben. (ez a feladat majdnem ugyan az, mint az előző feladat, 
csakhogy nincs load more gomb.) 
A megoldást egy scrollcatloader.py nevű fileban kell beadnod.
"""""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/scrolltoload.html")
actions = ActionChains(driver)
element = driver.find_element_by_xpath("/html/body/div[1]/div[20][@class ='image']")
actions.move_to_element(element).perform()

js = "window.scrollTo(0, 3000)"
driver.execute_script(js)
time.sleep(5)

local_file = 'c:\\cats'
cat_list = []


def image_data():
    for i in range(1, 21):
        element = driver.find_element_by_xpath(f"/html/body/div[1]/div[{i}][@class ='image']")
        data_row = {'sorszam': i}
        cat_id = element.find_element_by_tag_name("p").text
        cat_id = cat_id.replace("Cat id: ", "")
        data_row['cat_id'] = cat_id
        with open(f"{local_file}\\{data_row['sorszam']}_{data_row['cat_id']}.jpg", "w") as cat_log:
            cat_log.write(element.find_element_by_tag_name("img").get_attribute("src"))
        cat_list.append(data_row)


driver.quit()
