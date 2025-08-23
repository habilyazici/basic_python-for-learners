from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

url ="http://github.com"
driver.get(url)

print(driver.title)

if "GitHub · Build and ship software on a single, collaborative platform · GitHub" in driver.title:
    driver.save_screenshot("github-homepage.png")
time.sleep(2)

try:
    print(driver.find_element("tag name", "h1").text)
    print(driver.find_element("class name", "HeaderMenu-link").text)
    print(driver.find_element("id", "some-id").text)
    print(driver.find_element("css selector", "h1#nasılsın.merhaba").text)
    print(driver.find_element("css selector", "input[name='q']").get_attribute("placeholder"))
    print(driver.find_element("xpath", "//input[@name='q']").get_attribute("placeholder"))
    # result = driver.find_element("css selector", "div.some-class").find_element("tag name", "ul").find_element("tag name", "li").find_element("tag name", "a")
except Exception as e:
    print("Error occurred:", e)

searchButton = driver.find_element("css selector", "button[type='button'].header-search-button.input-button").click()
time.sleep(1)
searchInput = driver.find_element("css selector", "input[type='text'][spellcheck='false']#query-builder-test")
searchInput.send_keys("python")
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

a_list = driver.find_elements("css selector", "div.Box-sc-g0xbh4-0 h3 a")

for element in a_list:
    print(element.text)
time.sleep(2)

driver.execute_script("window.open('https://www.example.com')")
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.close()