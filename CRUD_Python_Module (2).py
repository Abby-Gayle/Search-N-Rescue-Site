# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username = 'aacuser', password = 'PikachuAbby'): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: #has data
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else: #no data
            return False      

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None: #has data
            result = list(self.database.animals.find(data)) #creates a list of data found
            return result #returns the data in a list
        else: #no data
            return [] #returns an empty list
    
    # Create method to implement the U in CRUD.
    def update(self, doc, data):
        if doc is not None and data is not None: #than can change data in document
            result = self.database.animals.update_many(doc, {"$set": data}) # changing as many as needed
            return "Altered Documents: " + str(result.modified_count)
        else: #document not found
            return "Document not found!"
    
    #Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None: #data found
            result = self.database.animals.delete_many(data) #delete the specific data
            return "Deleted Documents: " + str(result.deleted_count)
        else:
            return "Document not found!"
            