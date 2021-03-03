from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

r = requests.get("https://cache.dominos.com/nolo/ca/en/6_44_5/assets/build/market/CA/_en/templates/nationalCouponPageComponent.js")
url_to_scrape = "https://www.dominos.ca/en/pages/order/coupon"

print(r.text)
request_page = urlopen(url_to_scrape)
page_html = request_page.read()

request_page.close()

soup = BeautifulSoup(page_html, 'html.parser')

promo_items = soup.find('div', id="js-nationalCouponPage")
print(promo_items)

# This is not going to work.... :( - hidden HTML elements  - Will try Selenium. 

# for promo in promo_items:
#   img = promo.find('img')
#   print(promo)