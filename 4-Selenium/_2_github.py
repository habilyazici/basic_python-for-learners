from githubUserInfo import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        self.driver.maximize_window()

    def signIn(self):
        self.driver.get("https://github.com/login")
        time.sleep(2)

        self.driver.find_element("css selector", "form input.form-control#login_field[name='login']").send_keys(self.username)
        self.driver.find_element("xpath", "//*[@id='password']").send_keys(self.password)
        time.sleep(1)

        self.driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div/div[2]/form/div[3]/input").click()
        time.sleep(15)

    def loadFollowers(self):
        person_divs = self.driver.find_elements("css selector", "div.d-table.table-fixed")

        for div in person_divs:
            spans = div.find_elements("css selector", "a span")
            name = spans[0].text
            username_id = spans[1].text
            self.followers.append({"name": name, "username_id": username_id})
    def click_and_load(self, link):
        link.click()
        time.sleep(1)
        self.loadFollowers()
        print("Bu sayfadaki takipçiler kaydedildi")

    def getFollowers(self):
        self.driver.get(f"https://github.com/{self.username}?tab=followers")
        page_number = 1
        time.sleep(2)

        self.loadFollowers()
        while True:
            try:
                links = self.driver.find_element("class name", "BtnGroup").find_elements("tag name", "a")
                # biri önceki sayfa diğeri sonraki sayfa için
            except Exception as e:
                print("Hata:", e)
                break

            if len(links) == 1:
                if links[0].text == "Next":
                        self.click_and_load(links[0])
                        print(f"{page_number}. sayfadaki takipçiler kaydedildi")
                        page_number += 1
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                            self.click_and_load(link)
                            print(f"{page_number}. sayfadaki takipçiler kaydedildi")
                            page_number += 1
                    else:
                        continue

github = Github(username, password)

github.signIn()
github.getFollowers()
print(len(github.followers))
for dict in github.followers:
    print(f"{dict['name']} - {dict['username_id']}")

