from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()#specify path of your chrome driver

driver.get("https://www.facebook.com/?stype=lo&jlou=AffKTmFL36Y7HnIuV4cXQVQ6iJl3gnIqCmcZ_pVX3DmanfvW1kv44EGuQv2ZSERXzZpmBijfJRQixnXJwXiwg4zNFi-8V72NKum0UCYRrHeHzQ&smuh=56318&lh=Ac8i4A1sbOaXjTzO")
bhar=driver.find_element_by_id("email")
bhar.send_keys("id")#replace with your id
le=driver.find_element_by_id("pass")
le.send_keys("password")#replace with your password
le.send_keys(Keys.RETURN)
