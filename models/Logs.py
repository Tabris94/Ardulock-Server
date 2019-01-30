from mongoengine import Document, DateTimeField, StringField, ReferenceField
from models.Devices import Devices

class Logs(Document):
    time = DateTimeField(required = True)
    txt = StringField(required = True)
    Ardulock = ReferenceField(Devices, required = True)

