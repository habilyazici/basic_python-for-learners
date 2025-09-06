import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
# myclient = pymongo.MongoClient("mongodb+srv://habilyazici0:lhQwBfcB41NS3UDc@cluster0.v5us7cj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["new_database"]
mycollection = mydb["data_table1"]
# veri ekleme sonrasında olmayan database ve collection otomatik oluşur.

product = {"name": "Samsung S5", "price": 2000}

result = mycollection.insert_one(product)

print("eklenme sonucu: ", result)
print("eklenme sonucu type: ", type(result))
print("result.inserted_id: ", result.inserted_id)
print("result.inserted_id type: ", type(result.inserted_id))

print("\n" + 20 * '-' + "\n")

productList = [
    {"name":"Samsung S6", "price": 3000, "description":"0 telefon"},
    {"name":"Samsung S7", "price": 4000, "categories": ['telefon','tablet']},
    {"name":"Samsung S8", "price": 5000, "categories": ['telefon','elektronik'], "description":"0 telefon"},
    {"name":"Samsung S9", "price": 6000, "categories": ['telefon',], "description":"0 telefon"},
    {"name":"Samsung S10", "price": 7000, "categories": ['telefon','elektronik'], "description":"0 telefon"}
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)

myclient.close()