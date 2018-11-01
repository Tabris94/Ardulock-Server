from models.Users import Users
from mongoengine import *

def registrationController(body):
    if Users.objects(email = body.form['email']):
        return False
    else:
        newUser = Users(
            email = body.form['email'],
            first_name = body.form['first_name'],
            last_name = body.form['last_name'],
            password = body.form['password']
        )
        newUser.save()
        return True