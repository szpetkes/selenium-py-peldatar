"""""""""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/forms.html oldalt. Koncentrálj a dátum mezőkre. A célod, 
hogy a következő képen látható dátum és idő értékeket pontosan beállítsd az alkalmazásba selenium segítségével: 
assets/dates.png > A megoldást egy setdates.py nevű fileban kell beadnod.

setup1:  Date 06/05/2021
setup2:  Date/Time 2012.05.05 05:05:05:555
setup3:  Date/Time local 05/12/2000 12:01 PM
setup4:  Month December 1995
setup5:  Week Week 52, 2015
setup6:  Time 12:25 AM
 
"""""""""
from datetime import datetime, date

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/forms.html")

setup1 = date(2021, 6, 5)
driver.find_element_by_id("example-input-date").send_keys(setup1.strftime("%Y\t%mm%dd"))

setup2 = datetime(2012, 5, 5, 5, 5, 5, 555000)
driver.find_element_by_id("example-input-date-time").send_keys(setup2.strftime("%Y.%m.%d. %H:%M:%S:%f"))

setup3 = datetime(2000, 12, 5, 12, 1, 1, 1)
driver.find_element_by_id("example-input-date-time-local").send_keys(setup3.strftime("%Y\t/%m/%d%H:%M"))

setup4 = date(1995, 12, 1)
driver.find_element_by_id("example-input-month").send_keys(setup4.strftime("%Y\t%B"))

setup5 = date(2015, 12, 28)
driver.find_element_by_id("example-input-week").send_keys(setup5.strftime("%W%Y"))

setup6 = datetime(2012, 5, 5, 12, 25, 5, 555000)
driver.find_element_by_id("example-input-time").send_keys(setup6.strftime("%H%M"))
