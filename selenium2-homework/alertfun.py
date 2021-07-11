"""""""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
el a megoldás. Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar 
alkalmazást. A program töltse be a példatárból az http://localhost:9999/alert_playground.html oldalt. A tanultak 
alapján az összes alert funkcióra írj selenium kódot. A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e 
egy paragraf tagben, miután eltűnt az alert. A megoldást egy alertfun.py nevű fileban kell beadnod. 
"""""""""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

testdata = "RedAlert"

driver.get("http://localhost:9999/alert_playground.html")

driver.find_elements_by_xpath("//input[@type='button']")