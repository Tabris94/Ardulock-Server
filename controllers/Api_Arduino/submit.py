from models.Devices import Devices
from models.Users import Users
from mongoengine import *

def submit(body):

    #Se già esite lo elimino..
    if Devices.objects(mat = body['Seriale']):
        Devices.objects(mat = body['Seriale']).delete()

    newDevice = Devices(
        mat = body['Seriale'],
        labelFirstSensor = body['label1'],
        labelSecondSensor = body['label2'],
        statusFirstSensor = False,
        statusSecondSensor = False,
        unlockPassword = body['password'],
    )
    newDevice.save()

    #user = Users.objects(email = body['email'])
    #print(user)
    #Users[0].device = newDevice
    #Users[0].save

    try:
        Users.objects(email = body['email'])[0].device = newDevice
    except:
        print('Errore ..')

    return True