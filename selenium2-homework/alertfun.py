"""""""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
el a megoldás. Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar 
alkalmazást. A program töltse be a példatárból az http://localhost:9999/alert_playground.html oldalt. A tanultak 
alapján az összes alert funkcióra írj selenium kódot. A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e 
egy paragraf tagben, miután eltűnt az alert. A megoldást egy alertfun.py nevű fileban kell beadnod. 
"""""""""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver.get("http://localhost:9999/alert_playground.html")

driver.find_element_by_name('alert').click()
alert = driver.switch_to.alert
assert (alert.text == "I am alert")
print(alert.text)
alert.accept()

driver.find_element_by_name('confirmation').click()
alert = driver.switch_to.alert
assert (alert.text == "I am confirm")
print(alert.text)
alert.accept()

driver.find_element_by_name('prompt').click()
alert = driver.switch_to.alert
assert (alert.text == "I am prompt")
print(alert.text)
alert.send_keys("RedAlert")
alert.accept()

# assert driver.find_element_by_id('demo').text == 'RedAlert'
print(driver.find_element_by_id('demo').text)

# assert driver.find_element_by_id('demo').text == f"(You entered: {'RedAlert'}"

action = ActionChains(driver)
action.double_click(driver.find_element_by_id('double-click')).perform()
alert = driver.switch_to.alert
assert (alert.text == "You double clicked me!!!, You got to be kidding me")
print(alert.text)
alert.accept()

driver.quit()
