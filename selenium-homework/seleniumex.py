element_id = input('Kérem adja a keresendő ID t: ')
print('Keresem az oldalon a következő ID-t:', element_id)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("https://www.starwars.com/")

from selenium.common.exceptions import NoSuchElementException

try:
    hiba = driver.find_element_by_id(element_id)

except NoSuchElementException:
    print('Nem létezik ilyen element')
    driver.close()

else:
    print('Az oldalon található', element_id, 'elem')
