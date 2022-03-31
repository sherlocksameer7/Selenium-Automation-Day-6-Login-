from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

user_name = input("Enter Username: ")
pass_word = input("Enter Password: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
driver.find_element_by_name("username").send_keys(user_name)
time.sleep(3)
driver.find_element_by_name("password").send_keys(pass_word)
time.sleep(4)
driver.find_element_by_class_name("qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(10)

driver.close()
print("Testcase Completed")

