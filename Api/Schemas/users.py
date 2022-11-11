def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "profession": str(item["description"]),
        "phone" : int(item["phone"]),
        "imageUrl": str(item["imageUrl"]),
        "created_at": item["created_at"],
        "updated_at": item["updated_at"],
        "isActive": bool(item["imageUrl"]),
    }
    

def usersEntities(entities) -> list:
    return [userEntity(item) for item in entities]

