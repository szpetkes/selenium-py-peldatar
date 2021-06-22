from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("http://localhost:9999/kitchensink.html")

type_xpath = driver.find_elements_by_xpath("//div[@class='left-align']")
for x in range(len(type_xpath)):
    print("Következő elemet találtam:")
    print(type_xpath[x].text)

type_name = driver.find_element_by_name()
for x in range(len(type_name)):
    print(type_name[x].text)

type_id = driver.find_element_by_id()
for x in range(len(type_id)):
    print(type_id[x].text)
