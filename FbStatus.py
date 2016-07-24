from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user=raw_input("enter id")
password=raw_input("password")
status=raw_input("enter status to upload=")
driver = webdriver.Chrome("F:\chromedriver_win32\chromedriver")

driver.get("https://www.facebook.com/?stype=lo&jlou=AffKTmFL36Y7HnIuV4cXQVQ6iJl3gnIqCmcZ_pVX3DmanfvW1kv44EGuQv2ZSERXzZpmBijfJRQixnXJwXiwg4zNFi-8V72NKum0UCYRrHeHzQ&smuh=56318&lh=Ac8i4A1sbOaXjTzO")
driver.implicitly_wait(5)
bhar=driver.find_element_by_id("email")
bhar.send_keys(user)
le=driver.find_element_by_id("pass")
le.send_keys(password)
le.send_keys(Keys.RETURN)
bhar=driver.find_element_by_xpath("//*[@id='js_25']");
bhar.send_keys(status)
driver.find_element_by_xpath("//*[@id='u_0_16']/div[2]/div/div[2]/button").click()
