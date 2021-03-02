from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

PATH = "/home/nerdastic/chromedriver"
driver = webdriver.Chrome(PATH)

#driver.get("https://davidramalhoportfolio.herokuapp.com/")
driver.get("https://www.dominos.ca/en/pages/order/#!/locations/search/")

delivery_icon = driver.find_element_by_css_selector('#locationSearchForm > div > div.form__control-group.circ-icons > label.js-delivery.c-locationsearch-delivery > span.Delivery.c-delivery.circ-icons__icon.circ-icons__icon--delivery')
time.sleep(0.2)

delivery_icon.click()
time.sleep(0.2)

address = ['1223 ROSEHILL DR NW', 'CALGARY AB', 'T2K 1M3']
city_in_address = (address[1].split())[0]
province_in_address = (address[1].split())[1]

street = driver.find_element_by_id('Street')
street.click()
street.send_keys(address[0])

city = driver.find_element_by_id('City')
city.click()
city.send_keys(city_in_address)

province = Select(driver.find_element_by_id('Region'))
province.select_by_visible_text(province_in_address)

postal_code = driver.find_element_by_id('Postal_Code')
postal_code.click()
postal_code.send_keys(address[2])

continue_for_delivery = driver.find_element_by_css_selector('#locationSearchForm > div > div.form__control-group.form__control-group--actions--aligncenter > button')
continue_for_delivery.click()
time.sleep(2)

try:
    future = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#changeOrderTimingOverlay > div.card__body > form > fieldset > div > div:nth-child(2) > div > div.choose-future-time > select"))
    )
    use_future = driver.find_element_by_class_name('btn--future-time')
    future2 = driver.find_element_by_css_selector('#changeOrderTimingOverlay > div.card__body > form > fieldset > div > div:nth-child(2) > div > div.choose-future-time > select')
    future2.click()
    future2.send_keys(Keys.ARROW_DOWN)
    use_future.click()
except:
    print('no good')

time.sleep(1)

coupons_page = driver.find_element_by_css_selector('#_dpz > header > nav.nav.nav--primary > div.nav__inner > ul > li:nth-child(6) > a')
coupons_page.click()


# string = 'T2K 1M3'
# for letter in string:
#   time.sleep(0.1)
#   search.send_keys(letter)

# time.sleep(0.5)
# search.send_keys(Keys.RETURN)

# time.sleep(0.5)
# search.send_keys(Keys.RETURN)

# time.sleep(0.5)
# new_address = driver.find_element_by_id('HeaderAddressLabel').text
# print(new_address)

# #find_element_by_id('printLabel')