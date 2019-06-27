import pyexcel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
assert "Facebook" in driver.title
elem_email = driver.find_element_by_id("email")
elem_email.clear() 
elem_email.send_keys("XXXXXX")
elem_password = driver.find_element_by_id("pass")
elem_password.clear()
elem_password.send_keys("XXXXXX")
elem_password.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.find_element_by_xpath("//div[@id='userNavigationLabel']").click()
#driver.close()