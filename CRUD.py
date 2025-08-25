from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        #Initializing the MongoClient.
        #This helps to access the MongoDB databases and collections.
        #This is hard-wired to the aac database, the animal collection, and the aac user.

        #Connection Variables

        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30817
        DB = 'AAC'
        COL = 'animals'

        #Initialize Connection

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    #Create File
    def create(self, data):
        if data is not None:
            insertSuccess = self.collection.insert_one(data)
            #Insert was successful
            if insertSuccess:
                return True
            #Insert was not successful
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    #Read File
    def read(self, searchData):
        if searchData:
            data = self.collection.find(searchData)
        else:
            data = self.collection.find( {})
        return data
        
    #Update File
    def update(self, initialData, newData):
        if initialData:
            data = self.collection.update({initialData}, {"$set":newData})
            return True
        else:
            raise Exception("Nothing to update, because no result was found")
        return data
    
    def delete(self, deleteData):
        if deleteData:
            data = self.collection.delete(deleteData)
            return True
        else:
            raise Exception("Nothing to delete, because no result was found")
        return data