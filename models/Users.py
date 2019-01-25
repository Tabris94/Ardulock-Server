from mongoengine import Document, StringField, ReferenceField
from models.Devices import Devices
import string
import random
from uuid import uuid4

class Users(Document):
    email = StringField(required = True, unique = True)
    irst_name = StringField(max_lenght = 20, required = True)
    last_name = StringField(max_lenght = 20, required = True)
    password = StringField(min_lengt = 6, required = True)
    token = StringField(max_lenght = 20, unique = True)
    device = ReferenceField(Devices)

    def generate_token(self):
        token = str(uuid4())
        self.update(token = token)
        return token