from pymongo import MongoClient
import certifi

mongo_URI = "mongodb+srv://victorpolo:VictorPolo17@victor.r4ect.mongodb.net/"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(mongo_URI, tlsCAFile=ca)
        db = client['Hobbies']
        return db
    except ConnectionError:
        print("Error connecting to the database")
        return None

if __name__ == '__main__':
    db = dbConnection()
    if db is not None:
        print('SUCCESSFULLY CONECTION')