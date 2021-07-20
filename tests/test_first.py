from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:9999/randomajax.html")
    return driver


def test_first_testcase(browser):
    yes_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'yes')))
    yes_element.click()
    browser.find_element_by_id("buttoncheck").click()
    p = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="container"]/p')))
    print(p.text)


def test_second_testcase(browser):
    browser.get("https://google.com")
    time.sleep(2)
    assert True



driver.quit()
