from models.Users import Users
from models.Devices import Devices
from models.Logs import Logs

def getLogs(body):
    user = Users.objects(token = body['token'])
    if user: 
        return Logs.objects(Ardulock = user[0].device).order_by('-time')
        