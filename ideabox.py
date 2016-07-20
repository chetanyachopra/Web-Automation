from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()#you can replace Firefox with your Chrome driver if you want
driver.get("http://punjab.chitkara.edu.in//Interface/index.php")
bhar=driver.find_element_by_id("username")
bhar.send_keys("id")#enter your id here
bhar=driver.find_element_by_id("password")
bhar.send_keys("password")#enter your password here
bhar.send_keys(Keys.RETURN)
bhar=driver.find_element_by_id("ideaBox")
bhar.send_keys("")#enter your idea here
bhar.send_keys(Keys.RETURN)
