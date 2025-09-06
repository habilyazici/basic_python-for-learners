import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
# myclient = pymongo.MongoClient("mongodb+srv://habilyazici0:lhQwBfcB41NS3UDc@cluster0.v5us7cj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["new_database"]
mycollection = mydb["data_table1"]

print("\n" + 20 * '-' + "\n")
result = mycollection.find_one()
print(result)
print(type(result))
print(result["name"])
print("\n" + 20 * '-' + "\n")


for i in mycollection.find({},{"_id":0 ,"name": 1}):
    print(i)