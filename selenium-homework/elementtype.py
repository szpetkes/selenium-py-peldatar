from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("http://localhost:9999/trickyelements.html")

element_lista = []
for i in range(0, 5):
    számozás = str(i + 1)
    element = driver.find_element_by_id("element" + számozás)
    element_lista.append(element)

sorszam = 0
for lista_elem in element_lista:
    sorszam += 1
    lista_elem.click()
    result = driver.find_element_by_xpath('//label[@id="result"]')
    if result.text == f"{lista_elem.text} was clicked":
        print(format("Első button típusú elem:" + lista_elem.text))
        print("A szöveg helyes.")
        break
    elif result.text == "[Click any button]":
        print("A szöveg helyes, nem volt gomb található")
        continue
    else:
        print("A szöveg helytelen.")
