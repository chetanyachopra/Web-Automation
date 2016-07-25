import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user=raw_input("email=")
password=getpass.getpass("password=")
driver = webdriver.Firefox()
driver.get("http://www.gmail.com")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='Email']").send_keys(user)
driver.find_element_by_id("next").click()
driver.find_element_by_xpath("//*[@id='Passwd']").send_keys(password)
driver.find_element_by_xpath("//*[@id='signIn']").click()
driver.implicitly_wait(10)
driver.get("https://myaccount.google.com/")
driver.find_element_by_xpath("//*[@id='view_container']/div/div[2]/div/div[1]/a[3]/div/div[2]/div[2]/span").click()
driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[2]/div[1]/div").click()
driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div/div/div[2]").click()
driver.find_element_by_xpath("//*[@id='i2']/div[1]/div/div/div[2]/a[2]/div[2]").click()
