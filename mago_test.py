import pymongo
client = pymongo.MongoClient("mongodb+srv://mongo_db:abcd1234@cluster0.eudh50d.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)



dic = {
    "name": "Radhe",
    "emailid":"aswinikk@gmail.com",
    "surname":"Krishna"
}

dic = {
    "name": "Radhe",
    "emailid":"aswinikk@gmail.com",
    "surname":"Krishna"
}


dic = {
    "name": "Radhe",
    "emailid":"aswinikk@gmail.com",
    "surname":"Krishna"
}

dic = {
    "name": "Radhe",
    "emailid":"aswinikk@gmail.com",
    "surname":"Krishna"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(dic )
