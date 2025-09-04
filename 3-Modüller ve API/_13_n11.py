import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())


# list = soup.find("ul", attrs={"id":"listingUl", "class":"list-ul"}).find_all("li")

# for li in list:
#     name = li.div.a.h3.text.strip()
#     link = li.div.a.get("href")
#     newprice = li.find("div", attrs={"class":"proDetail"}).find("span", attrs={"class":"newprice"}).find("ins").text.strip()

#     print(f"name: {name} link: {link} new price: {newprice}")