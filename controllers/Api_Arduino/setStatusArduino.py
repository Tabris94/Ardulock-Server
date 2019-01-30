from models.Devices import Devices
from models.Logs import Logs
import datetime

def setStatusArduino(ard, matricola):
    dispositivo = Devices.objects(mat = matricola)[0]

    if ard.attivaZone(matricola, dispositivo.statusFirstSensor, dispositivo.statusSecondSensor) == "OK":
        return 200
    else:
        return 400

def archiviaLogArduino(matricola, logArd):
    dispositivo = Devices.objects(mat = matricola)[0]

    log = ""

    if logArd == "Z1-ALARM":
        log = "Allarme sensore Zona: " + dispositivo.labelFirstSensor
    elif logArd == "Z2-ALARM":
        log = "Allarme sensore Zona: " + dispositivo.labelSecondSensor
    elif logArd == "DIS-MAN":
        log = "Allarme Disattivato Manualmente"

    newLog = Logs(
        time = datetime.datetime.now,
        txt = log,
        Ardulock = dispositivo
    )
    newLog.save()