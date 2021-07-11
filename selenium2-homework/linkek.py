"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999 oldalt. Lokátorral keresd ki az összes linket az oldalról. 
Tárold a memóriában egy listában az összes linket. A list tartalmát írd ki egy fájlba. Minden link egy új sorba 
kerüljön. A kimenetre írd ki hány linket találtál 
A megoldást egy linkek.py nevű file-ban kell beadnod.
"""""""""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999")

links = driver.find_elements_by_xpath("//a")

szamlalo = 0

with open('links.txt', 'w') as linkek_listaja:
    for link in links:
        linkek_listaja.write(link.get_attribute('href') + '\n')
        szamlalo += 1

print("Az oldalon", len(links), 'linket találtam és kiírtam őket a links.txt fájlba.')
