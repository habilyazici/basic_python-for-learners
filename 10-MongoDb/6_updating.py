import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
# myclient = pymongo.MongoClient("mongodb+srv://habilyazici0:lhQwBfcB41NS3UDc@cluster0.v5us7cj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["new_database"]
mycollection = mydb["data_table1"]

print("Mevcut Veriler:")
for i in mycollection.find():
    print(i)
print("\n" + 20 * '-' + "\n")

mycollection.update_one(
    {'name': 'Samsung S6'}, 
    {'$set': {
        'name': 'IPhone 7',
        'price': 5000
    }}
)

filter = {'name': 'Samsung S7'}
newvalues = {'$set': {
                'name': 'IPhone 8',
                'price': 5000
            }} 

result = mycollection.update_many(filter, newvalues)

print(f'{result.modified_count} adet kayıt güncellendi.')

for i in mycollection.find():
    print(i)