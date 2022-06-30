from pymongo import MongoClient
myclient = MongoClient(
    'mongodb+srv://workshp:workshop123@cluster0.shpuc.mongodb.net/?retryWrites=true&w=majority')
mydb = myclient['test_db']
mycol = mydb['customers']
# listing databases
listdbs = mydb.list_collection_names()
print(listdbs)

mydict = {"name": 'rina', "address": "in ana's heart"}
# add one record to database
# x=mycol.insert_one(mydict)
mylist = [
    {"name": "Ahmed", "occupation": "bullied by farrina-twins"},
    {"name": "Farzana", "occupation": "Trainer Potato"},
    {"name": "Safrina", "occupation": "being annoying Traitors"},
    {"name": "Shika", "occupation": "bullying & Traitors"},
    {"name": "Hisham", "occupation": "everything his fault"},
    {"name": "Carol", "occupation": "Fancy hair"},
    {"name": "Irfan", "occupation": "supervisor for annoying kids & Traitor"},
    {"name": "Edmund", "occupation": "Traitor"},
    {"name": "ummu", "occupation": "kidocode godMother"},
    {"name": "Firdaus", "occupation": "superman"},
    {"name": "Hanis", "occupation": "cry-er tiktoker"},
    {"name": "Ruo xi", "occupation": "Already miss you"}
]
# add many records to database at once

# x=mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
# print(x.inserted_ids)
# find single documents
# x=mycol.find({},{ "_id": 0, "name": 1, "occupation": 1 })

# for i in x:
#   print(i)
# myquery = {"occupation": {"$gt": "S"}}
# myquery = { "occupation": { "$regex": "^F" } }

# mydoc = mycol.find().sort("name",-1)
# # # print(mydoc)
# for x in mydoc:
#     print(x)

# myquery = { "address": "in discord" }

# x=mycol.delete_one(myquery)
# print(x.deleted_count, " documents deleted.")
# mydoc = mycol.find().sort("name",-1)
# # # print(mydoc)
# for x in mydoc:
#     print(x)
# update single record
myquery = { "status": False }
newvalues = { "$set": { "status": True } }

x=mycol.update_one(myquery, newvalues)
print(x.modified_count,'documents updated')
""" 
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.") """
# mydoc = mycol.find({},{"_id":0}).sort("name",-1)
# # # print(mydoc)
# for x in mydoc:
#     print(x)
mydoc = mycol.find({},{"status":False})
print(mydoc)
for x in mydoc:
    print(x)
# ! dorp the whole collection 
# mycol.drop()