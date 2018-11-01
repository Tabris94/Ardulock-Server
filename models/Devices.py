from mongoengine import Document, StringField, BooleanField, StringField

class Devices(Document):
    mat = StringField(required = True)
    statusFirstSensor = BooleanField(required = True)
    statusSecondSensor = BooleanField(required = True)
    last_EndPoint = StringField(required = True)
