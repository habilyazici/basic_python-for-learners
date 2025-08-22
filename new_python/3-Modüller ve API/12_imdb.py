import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

yeni = soup.find_all("ul", attrs={"role": "presentation"})
print("Yeni:", yeni)