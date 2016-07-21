from selenium import webdriver
from selenium.webdriver.common.keys import Keys



user=input("Enter your chitkara id= ")
passs=raw_input("enter your password= ")
idea=raw_input("Now Let me know your innovative idea!! ")
print("Now sit back & relaax and enjoy the show do not touch your computer for few seconds")
driver=webdriver.Firefox()#you can replace Firefox with your Chrome driver if you want
driver.get("http://punjab.chitkara.edu.in//Interface/index.php")
bhar=driver.find_element_by_id("username")
bhar.send_keys(user)

bhar=driver.find_element_by_id("password")
bhar.send_keys(passs)
bhar.send_keys(Keys.RETURN)
bhar=driver.find_element_by_id("ideaBox")

bhar.send_keys(idea)
bhar.send_keys(Keys.RETURN)
