from pymongo import MongoClient
from Api.config.settings import Settings

settings = Settings()
MongoClient = MongoClient(settings.mongo_url)
db = MongoClient.UserData;