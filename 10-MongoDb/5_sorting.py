import pymongo

myclient = pymongo.MongoClient("mongodb+srv://habilyazici0:lhQwBfcB41NS3UDc@cluster0.v5us7cj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["new_databases"]
mycollection = mydb["datas"]

result = mycollection.find().sort('name', -1)
result = mycollection.find().sort([('name', 1), ('price', -1)])

print("\nSorted Results:")
for i in result:
    print(i)