from models.Users import Users
from mongoengine import *

def loginController(body):
    user = Users.objects(email = body['email'], password = body['password'])
    if user:
        return user[0].generate_token()
    else:
        return False