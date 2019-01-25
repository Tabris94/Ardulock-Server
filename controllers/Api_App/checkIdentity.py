from models.Users import Users

def checkIdentity(body):
    user = Users.objects(email = body['email'])
    if user[0].password == body['password']:
        return True
    return False