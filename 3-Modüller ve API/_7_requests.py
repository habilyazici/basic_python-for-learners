# HTTP istekleri göndermek için kullanılır (get,post,put,delete vb.)
import requests
import json

result1 = requests.get("https://jsonplaceholder.typicode.com/todos")
print(result1)
print(result1.status_code)

result2 = json.loads(result1.text)
result3 = result1.json()

print(type(result3))
i = 0
for user in result3:
    if user["userId"] == 1 and i < 8: 
        print(user["title"])
        print(user["id"])
        print("*")
        i += 1