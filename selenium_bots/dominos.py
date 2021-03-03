from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import address_fetch
import re

PATH = "/home/nerdastic/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.dominos.ca/en/pages/order/#!/locations/search/")

try:
    delivery = WebDriverWait(driver, 0.5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#locationSearchForm > div > div.form__control-group.circ-icons > label.js-delivery.c-locationsearch-delivery > span.Delivery.c-delivery.circ-icons__icon.circ-icons__icon--delivery"))
    )
    delivery_icon = driver.find_element_by_css_selector('#locationSearchForm > div > div.form__control-group.circ-icons > label.js-delivery.c-locationsearch-delivery > span.Delivery.c-delivery.circ-icons__icon.circ-icons__icon--delivery')
    delivery_icon.click()
    time.sleep(0.2)
except:
    print('Failed to Click on Delivery Icon')


address = address_fetch.address
city_in_address = (address[1].split())[0]
province_in_address = (address[1].split())[1]

time.sleep(0.2)
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

try:
    future = WebDriverWait(driver, 0.5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#changeOrderTimingOverlay > div.card__body > form > fieldset > div > div:nth-child(2) > div > div.choose-future-time > select"))
    )
    use_future = driver.find_element_by_class_name('btn--future-time')
    future2 = driver.find_element_by_css_selector('#changeOrderTimingOverlay > div.card__body > form > fieldset > div > div:nth-child(2) > div > div.choose-future-time > select')
    future2.click()
    future2.send_keys(Keys.ARROW_DOWN)
    use_future.click()
except:
    print('Local Dominos is Open :)')

time.sleep(1)

coupons_page = driver.find_element_by_css_selector('#_dpz > header > nav.nav.nav--primary > div.nav__inner > ul > li:nth-child(6) > a')
coupons_page.click()

time.sleep(0.3)

must_watch = driver.find_element_by_css_selector('#js-pageSplit > section > div.js-couponContainer > div > div.featured-coupon.promo.promo--featured.js-featuredCoupon.grid__cell--1.featured-coupon--top')
must_watch_coupon = re.split('; |, |\*|\n|   ', must_watch.text)

coupons_list = driver.find_elements_by_class_name("local-coupon")

print(len(coupons_list))

for coupon in coupons_list:
  x = re.split('; |, |\*|\n|   ', coupon.text)
  x.pop(0)
  #coupon = coupon.text.split('ADD COUPON')
  print(x)


#print(must_watch_coupon)