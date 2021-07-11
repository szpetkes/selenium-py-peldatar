"""""""""
Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a selenium-py-peldatar alkalmazást. A 
program töltse be a példatárból az http://localhost:9999/videos.html oldalt. Az oldalon találhotó összes beágyazott 
videót indítsa el és állítsa meg. 
A megoldást egy videoooo.py nevű fileban kell beadnod.
"""""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/videos.html")
video1 = driver.find_element_by_id("html5video")
video1.send_keys(Keys.SPACE)
time.sleep(3)
video1.send_keys(Keys.SPACE)

video2 = driver.find_element_by_xpath('//button[contains(text(), "Play/Pause")]')
video2.click()
time.sleep(3)
video2.click()

video3 = driver.find_element_by_id('youtubeframe')
video3.click()
time.sleep(3)
video3.click()

driver.quit()
