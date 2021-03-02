from selenium import webdriver

PATH = "/home/nerdastic/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://davidramalhoportfolio.herokuapp.com/")
print(driver.title)
driver.quit()
