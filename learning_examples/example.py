from urllib.request import urlopen
from bs4 import BeautifulSoup

# url_to_scrape = "https://www.dominos.ca/en/pages/order/coupon"
url_to_scrape = "https://davidramalhoportfolio.herokuapp.com/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

soup = BeautifulSoup(page_html, 'html.parser')

promo_items = soup.find_all('div', class_= 'service')

for promo in promo_items:
  img = promo.find_all('li')
  items = img
  for item in items:
    print(item.string.strip())