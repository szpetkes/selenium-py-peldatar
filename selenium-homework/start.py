from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("https://www.starwars.com/")

films = driver.find_element_by_class_name("films-content-title")
films.click()
