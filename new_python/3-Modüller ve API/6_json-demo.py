import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    newUser = User(username=user['username'], password=user['password'], email=user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı oluşturuldu.')
        print("\n" + 20 * '-' + "\n")

    def login(self, username, password):     
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapıldı.')
                print("\n" + 20 * '-' + "\n")
                break
        print('Kullanıcı adı veya şifre hatalı.')
        print("\n" + 20 * '-' + "\n")

    def logout(self):
        if not self.isLoggedIn:
            print('Giriş yapılmadı ki.')
            print("\n" + 20 * '-' + "\n")
            return
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı.')
        print("\n" + 20 * '-' + "\n")

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Giriş yaptıksan sonra lütfen tekrar deneyiniz.')
            print("\n" + 20 * '-' + "\n")

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(user.__dict__)
        with open('users.json','w', encoding='utf-8') as file:
            json.dump(list, file, ensure_ascii=False, indent=4)

repository = UserRepository()

while True:
    print('Menü'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')          
            password = input('password: ')          
            email = input('email: ')          

            user = User(username= username, password = password, email = email)
            repository.register(user)
        elif secim == '2':
            if repository.isLoggedIn:
                print('Zaten login oldunuz.')
                print("\n" + 20 * '-' + "\n")
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif secim == '3':
            repository.logout()
        elif secim == '4':
            repository.identity()
        else:
            print('Yanlış seçim')
            print("\n" + 20 * '-' + "\n")