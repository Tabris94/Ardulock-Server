from models.Users import Users
from models.Devices import Devices

def setStatusContoller(body):
    user = Users.objects(token = body['token'])
    if user:
        if user[0].device.unlockPassword == body['password']:
            if body['selector'] == 0:
                user[0].device.update(statusFirstSensor = bool(body['value']))
            else:
                user[0].device.update(statusSecondSensor = bool(body['value']))
            return 200
        return 400
    return 401