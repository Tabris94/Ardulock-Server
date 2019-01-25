from models.Users import Users
from mongoengine import *

def registrationController(body):
    if Users.objects(email = body['email']):
        return False
    else:
        newUser = Users(
            email = body['email'],
            first_name = body['first_name'],
            last_name = body['last_name'],
            password = body['password']
        )
        newUser.save()
        return True