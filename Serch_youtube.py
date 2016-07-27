from selenium import webdriver
from selenium.webdriver.common.keys import Keys
find=raw_input("what you want to search on youtube=")
driver=webdriver.Chrome("F:\chromedriver_win32\chromedriver")
driver.get("https://www.youtube.com/")
driver.find_element_by_xpath("//*[@id='masthead-search-term']").send_keys(find)
driver.find_element_by_xpath("//*[@id='search-btn']").click()
