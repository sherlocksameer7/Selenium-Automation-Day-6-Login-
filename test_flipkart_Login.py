from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

product = input("Enter any Product to Search: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()

driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(3)
driver.find_element_by_name("q").send_keys(product)
time.sleep(5)
driver.find_element_by_class_name("L0Z3Pu").click()
time.sleep(10)

driver.close()
print("Testcase Completed")