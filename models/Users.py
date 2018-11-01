from mongoengine import Document, StringField, ReferenceField
from Devices import Devices

class Users(Document):
    email = StringField(required = True, unique = True)
    first_name = StringField(max_lenght = 20, required = True)
    last_name = StringField(max_lenght = 20, required = True)
    password = StringField(min_lengt = 6, required = True)
    token = StringField(max_lenght = 20, required = True)
    device = ReferenceField(Devices)