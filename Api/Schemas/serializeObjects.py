
def serializeDict(entity) -> dict:
    if entity!=None:
        return {**{i:str(entity[i]) for i in entity if i=='_id'},**{i:entity[i] for i in entity if i!='_id'}}
    return None

def serializeList(entities) -> list:
    return [serializeDict(entity) for entity in entities]

