from model import dbConnection

class Hobbie():
    def __init__(self, user_id, name, info, percentage):
        self.user_id = user_id
        self.name = name
        self.info = info
        self.percentage = percentage

    def toDBCollection(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'information': self.info,
            'percentage': self.percentage
        }
    
# CREATE
def insertHobbie(hobbie):
    db = dbConnection()
    return db['hobbie'].insert_one(hobbie.toDBCollection())

# READ
def getAllHobbies(user_id):
    db = dbConnection()
    return list(db['hobbie'].find({'user_id': user_id}))

