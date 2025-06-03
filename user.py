from model import dbConnection
from bson.objectid import ObjectId

class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def toDBCollection(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    
# CREATE
def insertUser(user):
    db = dbConnection()
    return db['user'].insert_one(user.toDBCollection())

def getUser(email):
    db = dbConnection()
    return db['user'].find_one({'email': email})