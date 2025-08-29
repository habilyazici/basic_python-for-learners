from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.browser.maximize_window()

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element("xpath", "//*[@id='loginForm']/div[1]/div[1]/div/label/input")
        passwordInput = self.browser.find_element("xpath", "//*[@id='loginForm']/div[1]/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(4)
        self.browser.find_element("css selector", "header").find_elements("css selector", "section")[2].find_elements("css selector", "li")[1].find_element("css selector", "a").click()
        time.sleep(2)

        dialog = self.browser.find_element("css selector", "div[role=dialog]")

        def get_follower_divs():
            return self.browser.find_element(
                "xpath",
                "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div"
            ).find_elements("css selector", "div")

        print(f"first count: {len(get_follower_divs())}")
        time.sleep(2)

        action = webdriver.ActionChains(self.browser)

        while len(get_follower_divs()) < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(get_follower_divs())

            if len(get_follower_divs()) != newCount:
                followers = get_follower_divs()
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break

        followers = get_follower_divs()

        followerLinks = []
        i = 1
        for div in followers:
            link = div.find_element("css selector", "a").get_attribute("href")
            followerLinks.append(link)
            i += 1
            if i == max + 1:
                break

        with open("followers.txt", "w",encoding="UTF-8") as file:
            for link in followerLinks:
                file.write(link + "\n")

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element("tag name", "button")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element("tag name", "button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element("xpath", '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div').click()
            time.sleep(2)
        else:
            print("zaten takip etmiyorsunuz.")


instgrm = Instagram(username, password)
instgrm.signIn()
# instgrm.getFollowers(50)

instgrm.followUser('kod_evreni')
instgrm.unFollowUser('kod_evreni')