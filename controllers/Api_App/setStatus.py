from models.Users import Users
from models.Devices import Devices
from models.Logs import Logs
import datetime

def setStatusContoller(body):
    user = Users.objects(token = body['token'])
    if user:
        if user[0].device.unlockPassword == body['password']:
            user[0].device.update(statusFirstSensor = bool(body['first']))
            user[0].device.update(statusSecondSensor = bool(body['second']))
            newLog = Logs(
                time = datetime.datetime.now,
                txt = 'Variazione di stato - sensore 1: '+str(body['first'])+', sensore2: '+str(body['second']),
                Ardulock = user[0].device
            )
            newLog.save()
            return 200
        return 400
    return 401