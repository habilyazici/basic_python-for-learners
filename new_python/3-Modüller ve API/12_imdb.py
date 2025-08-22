import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
headers = {
    "User-Agent": "Mozilla/5.0"
}
html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, "html.parser")

li_list = soup.find('ul', attrs={"role": "presentation"}).find_all('li')
for li in li_list:
    film_adi = li.find('h3', attrs={"class": "ipc-title__text"}).string
    year = li.find('span', attrs={"class": "sc-15ac7568-7"}).string
    rating = li.find("div", attrs={"data-testid": "ratingGroup--container"}).find("span").find("span").string
    print(f"{film_adi}, Yıl: {year}, Rating: {rating}")