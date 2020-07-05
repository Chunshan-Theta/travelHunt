import pymongo
from bson import ObjectId
from pymongo.results import InsertOneResult
from Tblock import PlaceBlock, Block_core
from auth import MongoClientURL

client = pymongo.MongoClient(MongoClientURL)
print(client.list_database_names())


class db_query(object):
    def __init__(self, col:str):
        self.mydb = client["travelHunt"]
        self.mycol = self.mydb[col]

    def new_unit(self, owner:str, steps:[Block_core]):
        # auto generate id column called "_id"
        mydict = { "owner": owner, "steps": steps}
        query: InsertOneResult = self.mycol.insert_one(mydict)
        return query.inserted_id

    def new_place(self, place_dict: PlaceBlock):
        # auto generate id column called "_id"
        query: InsertOneResult = self.mycol.insert_one(place_dict)
        return query.inserted_id

    ###

    def _find(self, **kwargs):
        projection = kwargs.pop("projection", None)
        if projection is None:
            return list(self.mycol.find(filter=kwargs))
        else:
            return list(self.mycol.find(filter=kwargs, projection=projection))

    def _delete_by_id(self, _id:str):
        _id = ObjectId(_id)
        self.mycol.delete_one(filter={"_id": _id})

    ###

    def set_col_to_unit(self):
        self.mycol = self.mydb['unit']

    def set_col_to_place(self):
        self.mycol = self.mydb['place']

    def get_col(self):
        return self.mycol


"""
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x: InsertManyResult = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x, x.inserted_ids)
"""
