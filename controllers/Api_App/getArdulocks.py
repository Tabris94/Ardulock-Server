from models.Users import Users
from models.Devices import Devices

def getArdulocksController(body):
    user = Users.objects(token = body['token'])
    if user:
        if user[0].device:
            return user[0].device
        return 400
    return 401