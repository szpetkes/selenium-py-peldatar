"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/pagination.html oldalt. Mentsd le az összes kontaktot az 
oldalról akinek a keresztneve (First Name) A betüvel kezdődik. A kiválasztott kontaktok összes adatát mentsd le 
memóriába egy szotár (dict) struktúrába. Amikor megvagy az összes adatot mentsd ki egy CSV file-ba. 

A megoldást egy pagination.py nevű fileban kell beadnod.
"""""

import csv
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

my_list = []

try:
    driver.get("http://localhost:9999/pagination.html")
    while True:
        table = driver.find_element_by_xpath('//table[@id="contacts-table"]/tbody')
        rows = table.find_elements_by_tag_name("tr")
        time.sleep(2)
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["First name"] = cells[1].text
            data_row["Second name"] = cells[2].text
            data_row["Surname"] = cells[3].text
            data_row["Second Surname"] = cells[4].text
            data_row["Birth date"] = cells[5].text
            if str.startswith(data_row["First name"], 'A'):
                my_list.append(data_row)
        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()

finally:
    keys = my_list[0].keys()
    with open('pagination.csv', 'a', newline='', encoding='utf-8') as fileA:
        writer = csv.DictWriter(fileA, keys)
        writer.writerows(my_list)
    driver.quit()
