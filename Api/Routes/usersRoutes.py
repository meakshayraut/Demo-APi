from bson import objectid
from fastapi import status, File, UploadFile
from Api.models.users import CreateUser
from Api.Routes.utils import getResponse, riseHttpExceptionIfNotFound
from Api.helpers.save_picture import save_picture
from Api.Services import usersService as service
from fastapi import APIRouter

userRoutes = APIRouter()
base = '/users/'
UploadImage = f'{base}image-upload/'

_notFoundMessage = "Could not find user with the given Id."


@userRoutes.get(base)
async def getAll():
    return await service.getAllUser()


@userRoutes.get(base+'{id}')
async def getById(id):
    return await resultVerification(id)   
  

@userRoutes.post(base)
async def InsertUser(data: CreateUser):
    return await service.InsertUser(data)


@userRoutes.put(base+'{id}', status_code=status.HTTP_204_NO_CONTENT)
async def updateUser(id, data: CreateUser):
    await resultVerification(id)
    done : bool = await service.updateUser(id,data);
    return getResponse(done, errorMessage="An error occurred while editing the user information.")


@userRoutes.delete(base+'{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(id):
    await resultVerification(id)
    done : bool = await service.deleteUser(id);
    return getResponse(done, errorMessage="There was an error.")   


@userRoutes.post(UploadImage+'{id}', status_code=status.HTTP_204_NO_CONTENT)
async def uploadUserImage(id: str, file: UploadFile = File(...)):
    result = await resultVerification(id)
    imageUrl = save_picture(file=file, folderName='users', fileName=result['name'])
    done = await service.savePicture(id, imageUrl)
    return getResponse(done, errorMessage="An error occurred while saving user image.")



# Helpers

async def resultVerification(id: objectid) -> dict:
    result = await service.getById(id)
    await riseHttpExceptionIfNotFound(result, message=_notFoundMessage)
    return result
