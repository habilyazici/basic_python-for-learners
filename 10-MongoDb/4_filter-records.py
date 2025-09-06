import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://habilyazici0:lhQwBfcB41NS3UDc@cluster0.v5us7cj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["new_databases"]
mycollection = mydb["datas"]

result = mycollection.find_one({"name": "Samsung S5"})
print(result)
result = mycollection.find_one({"_id": ObjectId("68bbec8166d4c87966e1e69d")})
print(result)
print("\n" + 20 * '-' + "\n")

'''
MongoDB sorgu operatörleri Türkçe açıklamaları:
$eq  : Alanın değeri belirtilen değere eşitse eşleşir. (eşittir)
$ne  : Alanın değeri belirtilen değere eşit değilse eşleşir. (eşit değildir)
$gt  : Alanın değeri belirtilen değerden büyükse eşleşir. (büyüktür)
$gte : Alanın değeri belirtilen değerden büyük veya eşitse eşleşir. (büyük veya eşittir)
$lt  : Alanın değeri belirtilen değerden küçükse eşleşir. (küçüktür)
$lte : Alanın değeri belirtilen değerden küçük veya eşitse eşleşir. (küçük veya eşittir)
$in  : Alanın değeri verilen dizi diziden biriyle eşleşirse eşleşir. (dizi içinde varsa)
$and : Tüm verilen sorgu koşulları sağlanıyorsa eşleşir. (ve)
$or  : Verilen sorgu koşullarından en az biri sağlanıyorsa eşleşir. (veya)
$nor : Verilen sorgu koşullarından hiçbiri sağlanmıyorsa eşleşir. (ne ... ne)
$not : Belirtilen sorgu koşulunu sağlamayan belgelerle eşleşir. (değil)
'''

filter = {
    "name": {
        "$in" : ["Samsung S5","Samsung S10"]
    }
}
result = mycollection.find(filter)
print(type(result))
for i in result:
    print(i)
print("\n" + 20 * '-' + "\n")

result = mycollection.find({
    "$and": [
        {"price": {"$gt": 1000}},
        {"name": "Samsung S5"}
    ]
})
print("AND sorgusu:")
for i in result:
    print(i)
print("\n" + 20 * '-' + "\n")

result = mycollection.find({
    "$or": [
        {"price": {"$lt": 1000}},
        {"name": "Samsung S5"}
    ]
})
print("OR sorgusu:")
for i in result:
    print(i)
print("\n" + 20 * '-' + "\n")

result = mycollection.find({
    "price": {
        "$not": {"$gt": 1000}
    }
})
print("NOT sorgusu:")
for i in result:
    print(i)
print("\n" + 20 * '-' + "\n")

result = mycollection.find({
    "$nor": [
        {"price": {"$lt": 1000}},
        {"name": "Samsung S5"}
    ]
})
print("NOR sorgusu(and'in olumsuzu):")
for i in result:
    print(i)
print("\n" + 20 * '-' + "\n")

result = mycollection.find({
    "name": { "$regex": "^S" }
})
print("Regex sorgusu:")
for i in result:
    print(i)