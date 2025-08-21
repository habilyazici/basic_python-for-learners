# HTTP istekleri göndermek için kullanılır (get,post,put,delete vb.)
import requests
import json

result1 = requests.get("https://jsonplaceholder.typicode.com/todos")
print(result1.status_code)

result2 = json.loads(result1.text)
result3 = result1.json()

print(type(result3))
for i in result3:
    if i["userId"] == 1: 
        print(i["title"])
        print("*")