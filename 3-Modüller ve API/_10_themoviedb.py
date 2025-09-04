# themoviedb.org 
import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZWM2N2ViNDhiM2Q0OGY0MmI3YzNmNjcwNTU0OGNhNiIsIm5iZiI6MTc1NTgwMzQzNi4zODIwMDAyLCJzdWIiOiI2OGE3NmYyYzk3NDQwNTAxNTlkNTUxN2MiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.tz8SN4V8XhhxTGXOB_ma9GX1bsZ5cm1eXTlpqqjDeQQ"
        self.headers = {
            "Authorization": "Bearer " + self.api_key,
            "Accept": "application/json"
        }

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1", headers=self.headers)
        movies = response.json()
        for idx, movie in enumerate(movies['results'], 1):
            print(f"{idx}. {movie['title']}")

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/movie?query={keyword}&include_adult=false&language=en-US&page=1", headers=self.headers)
        movies = response.json()
        for idx, movie in enumerate(movies['results'], 1):
            print(f"{idx}. {movie['title']}")

movieApi = theMovieDb()

while True:
    secim = input("1-Popular Movies\n2-Search Movies\n3-Exit\nSeçim: ")                
    if secim == "3":
        break
    else:
        if secim == "1":
            movieApi.getPopulars()

        if secim == "2":
            keyword = input('keyword: ')
            movieApi.getSearchResults(keyword)