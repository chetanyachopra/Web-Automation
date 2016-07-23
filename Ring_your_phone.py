from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user=raw_input("email=")
password=raw_input("password=")
driver = webdriver.Firefox()
driver.get("http://www.gmail.com")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='Email']").send_keys(user)
driver.find_element_by_id("next").click()
driver.find_element_by_xpath("//*[@id='Passwd']").send_keys(password)
driver.find_element_by_xpath("//*[@id='signIn']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='gbwa']/div[1]/a").click()
driver.find_element_by_xpath('//*[@id="gb192"]/span[1]').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='view_container']/div/div[2]/div/div[1]/a[3]/div/div[2]/div[1]").click()
