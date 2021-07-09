"""""""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
el a megoldás. Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar 
alkalmazást. A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt. Gyakorlás képpen 
keress ki elemeket a képernyőről az alábbi kritériumoknak megfelelően: ID alapján NAME alapján XPath kifejezéssel 
Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét. """

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())


def get_attr():
    print(multi_select_apple.get_attribute("value"))
    print(bmw_check.get_attribute("value"))
    print(confirm_button.get_attribute("type"))


try:
    driver.get("http://localhost:9999/kitchensink.html")
    driver.find_element_by_id("bmwradio")
    driver.find_element_by_id("carselect")
    driver.find_element_by_name("enter-name")
    driver.find_element_by_name("show-hide")
    multi_select_apple = driver.find_element_by_xpath('//select[@id="multiple-select-example"]/option[1]')
    bmw_check = driver.find_element_by_xpath('//input[@id="bmwcheck"]')
    confirm_button = driver.find_element_by_id("confirmbtn")
    get_attr()
    print("test finished OK")
except NoSuchElementException as no_element:
    print('Element not found: ', no_element)
driver.quit()
