from mongoengine import Document, StringField, BooleanField, StringField, IntField

class Devices(Document):
    mat = StringField(required = True)
    labelFirstSensor = StringField(max_lenght = 20, required = True)
    labelSecondSensor = StringField(max_lenght = 20, required = True)
    statusFirstSensor = BooleanField(required = True)
    statusSecondSensor = BooleanField(required = True)
    unlockPassword = StringField(min_length = 6)
    last_EndPoint = IntField()#StringField()
