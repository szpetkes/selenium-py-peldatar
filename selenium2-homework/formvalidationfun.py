"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/simplevalidation.html oldalt. A tanultak alapján teszteld le 
az űlap mező ellőnőrző funkcióit. 
A megoldást egy formvalidationfun.py nevű fileban kell beadnod.
"""""""""""
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/simplevalidation.html")
driver.find_element_by_id("test-email").send_keys("testemail")

input1 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='e-w11uh9t9']"))).get_attrubite("validationMessage")
assert input1 is None
assert input1 == "Please check your E-Mail format"

driver.find_element_by_name("Password").click()
input2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='e-w11uh9t9']"))).get_attrubite("validationMessage")

assert input2 is None
assert input2 == "This field can't be empty"

driver.find_element_by_id("e-ami9ay1w").click()
