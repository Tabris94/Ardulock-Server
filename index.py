from flask import Flask, request
from flask import Response
from mongoengine import *
from controllers.Api_App.registration import registrationController

app = Flask(__name__)
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/ArduLock'
app.debug = True

connect('Ardulock-db', host='localhost', port=27017)

@app.route("/")
def index():
    return 'hello world'

@app.route("/Api/App/registration", methods=['POST'])
def registration():
    if registrationController(request):
        return Response('', status = 200, mimetype='application/json')
    return Response('', status = 400, mimetype='application/json')

if __name__ == "__main__":
    app.run()