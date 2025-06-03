from model import dbConnection

class Hobbie():
    def __init__(self, user_id, hobbie, info, percentage):
        self.user_id = user_id
        self.hobbie = hobbie
        self.info = info
        self.percentage = percentage

    def toDBCollection(self):
        return {
            'user_id': self.user_id,
            'hobbie': self.hobbie,
            'information': self.info,
            'percentage': self.percentage
        }
    
# CREATE
def insertHobbie(hobbie):
    db = dbConnection()
    return db['hobbie'].insert_one(hobbie.toDBCollection())

# READ
def getAllHobbies():
    db = dbConnection()
    return list(db['hobbie'].find())

