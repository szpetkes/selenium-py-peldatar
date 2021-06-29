"""""""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
el a megoldás. Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar 
alkalmazást. A program töltse be a példatárból az http://localhost:9999/todo.html oldalt. A feladatod, hogy kigyűjtsd 
az összes jelenleg aktív Todo bejegyzést. Ha lehet akkor ezt minnél kevesebb selenium lokátorral old meg. (Tökéletes 
megoldáshoz csak egy darab find_by hívásra van szükség). "" """

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("http://localhost:9999/todo.html")

try:
    todo_list = driver.find_elements_by_class_name("done-false")

    for i in todo_list:
        print(i.text)
        time.sleep(1)

finally:
    driver.close()
