# json verisi tırnak işareti ile tanımlanır.
print("\n" + 20 * '-')
import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

dict = {"name": "Ali", "languages": ["Python", "Java"]}
dict_list = [
    {"name": "Ali", "languages": ["Python", "Java"]},
    {"name": "Ayşe", "languages": ["C#", "JavaScript"]},
    {"name": "Mehmet", "languages": ["Go", "Rust"]},
    {"name": "Fatma", "languages": ["Python", "Ruby"]}
]

person_json_string = '{"name": "Ali", "languages": ["Python", "Java"]}'
person_json_string = '[{"name": "Ali", "languages": ["Python", "Java"]},{"name": "Ayşe", "languages": ["C#", "JavaScript"]},{"name": "Mehmet", "languages": ["Go", "Rust"]},{"name": "Fatma", "languages": ["Python", "Ruby"]}]'

# JSON string to python, dosya üzerinde işlemlerde tekil olarak kullan
loads = json.loads(person_json_string)
print(loads)
print(type(loads))
for user in loads:
    print(user["name"], user["languages"])
print("\n" + 20 * '-')

with open("users.json", encoding="utf-8") as f:
    load = json.load(f)
    for user in load:
        print(user["username"], user["password"], user["email"])
print("\n" + 20 * '-')

# Python to JSON string, indent kullanmazsan direkt sıfır boşluksuz bir satıra yazar 
dumps = json.dumps(dict, sort_keys= True, ensure_ascii=False)
print("json stringi:", dumps)
print(type(dumps))

with open("person.json", "w" , encoding="utf-8") as f:
    json.dump(dict, f, indent=4, sort_keys= True, ensure_ascii=False)
    print("JSON dosyasına yazıldı.")
print("\n" + 20 * '-')