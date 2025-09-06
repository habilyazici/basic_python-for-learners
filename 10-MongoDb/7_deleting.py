import pymongo

myclient = pymongo.MongoClient("mongodb+srv://habilyazici0:lhQwBfcB41NS3UDc@cluster0.v5us7cj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["new_databases"]
mycollection = mydb["datas"]

for i in mycollection.find():
    print(i)
print("\n" + 20 * '-' + "\n")

# mycollection.delete_one({"name": "IPhone 8"})
# mycollection.delete_many({"name": {"$regex":"^S"}})
result = mycollection.delete_many({})

print(f'{result.deleted_count} adet kayıt silindi.')

for i in mycollection.find():
    print(i)