""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/editable-table.html oldalt. A megjelenő táblázatban az
alábbi feladatokat kell végrehajtanod:

a) Addj hozzá még két teljesen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
b) Ellenőrizd a kereső funkciót.
c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:9999/editable-table.html')

testdata1 = ["book", "11.99", "3", "Books"]
testdata2 = ["pen", "1.49", "10", "Stationeries"]
testdata3 = "pen"
testdata4 = ["pencil", "2.49", "15", "Stationers"]

add_button = driver.find_element_by_xpath('//button[text()="Add"]')


def input_data1():
    add_button.click()
    line_number = len(driver.find_elements_by_xpath("//tr[@class='eachRow']"))

    field = driver.find_elements_by_xpath(
        f"//table[@class='table table-bordered']/tbody/tr[{line_number}]/td/input")
    for i in range(len(testdata1)):
        field[i].send_keys(testdata1[i])
    assert len(driver.find_elements_by_xpath("//tr[@class='eachRow']")) == line_number


input_data1()


def input_data2():
    add_button.click()
    line_number = len(driver.find_elements_by_xpath("//tr[@class='eachRow']"))

    field = driver.find_elements_by_xpath(
        f"//table[@class='table table-bordered']/tbody/tr[{line_number}]/td/input")
    for i in range(len(testdata1)):
        field[i].send_keys(testdata2[i])
    assert len(driver.find_elements_by_xpath("//tr[@class='eachRow']")) == line_number


input_data2()

search_field = driver.find_element_by_tag_name('input')
search_field.clear()
search_field.send_keys(testdata3)
add_button.click()
