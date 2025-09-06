import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://habilyazici0:lhQwBfcB41NS3UDc@cluster0.v5us7cj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
print("myclient yazdırılmış hali:  ", myclient)
print(myclient.list_database_names())

mydb = myclient["new_databases"] 
print(mydb)
print("\n" + 20 * '-' + "\n")

print(type(mydb))
print(dir(mydb))
print("\n" + 20 * '-' + "\n")
print(mydb.list_collection_names())

print("\n" + 20 * '-' + "\n")
mycollection = mydb["datas"]
print(mycollection)

myclient.close()