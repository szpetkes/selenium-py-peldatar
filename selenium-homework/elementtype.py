"""""""""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható 
el a megoldás. Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar 
alkalmazást. A program töltse be a példatárból az http://localhost:9999/trickyelements.html oldalt. Használj id 
lokátort és keressd ki az elemenekt egyesével. A legelső olyan elemre ami button típusú kattints rá és ellenőrizd, 
hogy a helyes szöveg jelenik-e meg az elemek listája alatt.  "" """


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
    szamozas = str(i + 1)
    element = driver.find_element_by_id("element" + szamozas)
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
        
# try:
#    driver.get("http://localhost:9999/trickyelements.html")
#    found_elements = [driver.find_element_by_id("element1"), driver.find_element_by_id("element2"), driver.find_element_by_id("element3"),
#                      driver.find_element_by_id("element4"), driver.find_element_by_id("element5")]
#    for element in found_elements:
#        if element.tag_name == "button" or element.get_attribute("onclick") is not None:
#            button_text = element.text
#            element.click()
#            break
#    message_text = driver.find_element_by_id("result").text
#    assert f'{button_text} was clicked' == message_text
#    print("test finished OK")
#
# except NoSuchElementException as e:
#    print('Element not found: ', e)
#     driver.close()
