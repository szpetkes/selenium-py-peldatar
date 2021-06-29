"""""""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
el a megoldás. Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar 
alkalmazást. A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt. Gyakorlás képpen 
keress ki elemeket a képernyőről az alábbi kritériumoknak megfelelően: ID alapján NAME alapján XPath kifejezéssel 
Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét. """

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("http://localhost:9999/kitchensink.html")


search_element = driver.find_element_by_xpath('//*[@id="radio-btn-example"]').text
print(search_element)

search_element = driver.find_element_by_id('radio-btn-example').text
print(search_element)

search_element = driver.find_element_by_name('cars').text
print(search_element)

