from selenium import webdriver
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

url = "http://github.com"
driver.get(url)

driver.maximize_window()
time.sleep(2)
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/sadikturan"
driver.get(url)
print(driver.current_url)
driver.refresh()
time.sleep(2)

if "sadikturan (Sadık Turan) · GitHub" in driver.title:
    driver.save_screenshot("github-sadikturan.png")
time.sleep(2)

driver.back()
# driver.forward()
time.sleep(2)
driver.close()

