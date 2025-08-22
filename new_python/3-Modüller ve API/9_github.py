import json
import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "Accept": "application/vnd.github.v3+json"
        }

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+ username)
        result = response.json()
        print(f"name: {result['name']} public repos: {result['public_repos']}  follower : {result['followers']}")
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+ username+'/repos')
        result = response.json()
        for repo in result:
            print(repo['name'])    

    def createRepository(self, name):
        response = requests.post(self.api_url+'/user/repos', headers=self.headers, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username= input('username: ')
            result = github.getUser(username)
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result) 
        else:
            print('yanlış seçim') 
