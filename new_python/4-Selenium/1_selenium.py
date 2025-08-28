from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

url = "http://github.com"
driver.execute_script(f"window.open('{url}')")
driver.switch_to.window(driver.window_handles[-1])

time.sleep(2)
url = "http://github.com/sadikturan"
driver.get(url)
print(driver.current_url)
driver.refresh()
time.sleep(2)

driver.back()
# driver.forward()
time.sleep(2)

print(driver.title)

if "GitHub · Build and ship software on a single, collaborative platform · GitHub" in driver.title:
    driver.save_screenshot("github-homepage.png")
time.sleep(2)

try:
    result1 = driver.find_element("tag name", "h1").text
    result2 = driver.find_element("class name", "HeaderMenu-link").text
    result3 = driver.find_element("id", "some-id").text

    result4 = driver.find_element("css selector", "h1#nasılsın.merhaba").text
    result5 = driver.find_element("css selector", "input[name='q']").get_attribute("placeholder")
    result6 = driver.find_element("xpath", "//input[@name='q']").get_attribute("placeholder")
    result7 = driver.find_element("css selector", "div.some-class").find_element("tag name", "ul").find_element("tag name", "li").find_element("tag name", "a")

    results = [result1, result2, result3, result4, result5, result6, result7]
    for result in results:
        print(result)
        
except Exception as e:
    print("Hata bulundu:", e)

searchButton = driver.find_element("css selector", "button[type='button'].header-search-button.input-button").click()
time.sleep(2)
searchInput = driver.find_element("css selector", "input[type='text'][spellcheck='false']#query-builder-test")
searchInput.send_keys("python")
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

a_list = driver.find_elements("css selector", "div.Box-sc-g0xbh4-0 h3 a")

for a_element in a_list:
    print(a_element.text)
time.sleep(2)

driver.execute_script("window.open('https://www.example.com')")
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.close()