from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("https://happy-sea-0a5ffef03.azurestaticapps.net/masodik.html")

driver.get("https://happy-sea-0a5ffef03.azurestaticapps.net/masodik.html")
driver.find_element(By.XPATH, "//div[@id=\'container\']/input").click()
driver.find_element(By.XPATH, "//div[@id=\'container\']/input").send_keys("new todo")
driver.find_element(By.XPATH, "//div[@id=\'container\']/ul/li").click()
driver.find_element(By.XPATH, "//i[@id=\'plus-icon\']").click()
driver.find_element(By.XPATH, "//div[@id=\'container\']/ul/li/span/i").click()
