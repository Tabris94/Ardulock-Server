from models.Devices import Devices

def setStatusArduino(ard, matricola):
    dispositivo = Devices.objects(mat = matricola)

    if ard.attivaZone(matricola, dispositivo.statusFirstSensor, dispositivo.statusSecondSensor) == "OK":
        return 200
    else:
        return 400
