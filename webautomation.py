from selenium import webdriver

driver=webdriver.Chrome("C:\Python27\chromedriver_win32\chromedriver")
driver.get("www.google.com")
driver.quit()
