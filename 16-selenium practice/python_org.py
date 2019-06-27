from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_id("id-search-field")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
driver.close()