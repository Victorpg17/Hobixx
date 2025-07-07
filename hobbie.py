from model import dbConnection

class Hobbie():
    def __init__(self, user_id, hobbie, info, hours, minutes):
        self.user_id = user_id
        self.hobbie = hobbie
        self.info = info
        self.hours = hours
        self.minutes = minutes

    def toDBCollection(self):
        return {
            'user_id': self.user_id,
            'hobbie': self.hobbie,
            'information': self.info,
            'hours': self.hours,
            'minutes': self.minutes
        }
    
# CREATE
def insertHobbie(hobbie):
    db = dbConnection()
    return db['hobbie'].insert_one(hobbie.toDBCollection())

# READ
def getAllHobbies(user_id):
    db = dbConnection()
    return list(db['hobbie'].find({'user_id': user_id}))

