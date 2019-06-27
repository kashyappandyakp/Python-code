from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get ("https://www.hotstar.com/")
assert "Hotstar - Watch TV Shows,Movies,Live Cricket Matches & News Online" in driver.title

elem = driver.find_element_by_id("searchField")
elem.clear()
elem.send_keys("Cricket")
elem.send_keys(Keys.RETURN)