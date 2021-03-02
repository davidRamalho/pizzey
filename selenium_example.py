from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/home/nerdastic/chromedriver"
driver = webdriver.Chrome(PATH)

#driver.get("https://davidramalhoportfolio.herokuapp.com/")
driver.get("https://www.canadapost.ca/info/mc/personal/postalcode/fpc.jsf")

search = driver.find_element_by_id('addressComplete')
search.click()
string = 'T2R 0H8'
for letter in string:
  time.sleep(0.1)
  search.send_keys(letter)

time.sleep(0.5)
search.send_keys(Keys.RETURN)

time.sleep(0.5)
search.send_keys(Keys.RETURN)

time.sleep(0.5)
new_address = driver.find_element_by_id('HeaderAddressLabel')
print(new_address.text)

#find_element_by_id('printLabel')