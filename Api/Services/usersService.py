from bson import ObjectId
from Api.config.db import db
from Api.models.Dto.CreateUser import CreateUser
from Api.Schemas.serializeObjects import serializeDict, serializeList


async def getAllUser() -> list:
    return serializeList(db.users.find())


async def getById(id):
    return serializeDict(db.users.find_one({"_id": ObjectId(id)}))    


async def InsertUser(data: CreateUser):
    result = db.users.insert_one(dict(data))
    return serializeDict(db.users.find_one({"_id": ObjectId(result.inserted_id)}))


async def updateUser(id, data: CreateUser) -> bool:
    db.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(data)})
    return True

async def savePicture(id, imageUrl: str) -> bool:
    db.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": { "imageUrl": imageUrl }})
    return True


async def deleteUser(id) -> bool:
    db.users.find_one_and_delete({"_id": ObjectId(id)})
    return True






