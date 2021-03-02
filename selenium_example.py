from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

PATH = "/home/nerdastic/chromedriver"
driver = webdriver.Chrome(PATH)

#driver.get("https://davidramalhoportfolio.herokuapp.com/")
driver.get("https://www.canadapost.ca/info/mc/personal/postalcode/fpc.jsf")

search = driver.find_element_by_id('addressComplete')
search.click()
string = 'T2K 1M3'
for letter in string:
  time.sleep(0.1)
  search.send_keys(letter)

time.sleep(1)
search.send_keys(Keys.RETURN)

time.sleep(1)
search.send_keys(Keys.RETURN)

try:
    new_address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#HeaderAddressLabel > br"))
    )
    new_address = driver.find_element_by_id('HeaderAddressLabel').text
    address = re.split('; |, |\*|\n|   ', new_address)
    print(address)
except:
    driver.quit()





#find_element_by_id('printLabel')