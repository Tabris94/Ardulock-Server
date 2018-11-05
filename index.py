from flask import Flask, request 
from flask_cors import cross_origin
from flask import Response
import json
from mongoengine import *
from controllers.Api_App.registration import registrationController
from controllers.Api_App.login import loginController

app = Flask(__name__)
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/ArduLock'
app.debug = True
app.config['CORS_ORIGINS'] = "*"
app.config['CORS_HEADERS'] = ['Content-Type']

connect('Ardulock-db', host='localhost', port=27017)

@app.route("/")
@cross_origin()
def index():
    return 'hello world'

@app.route("/Api/App/registration", methods=['POST'])
@cross_origin()
def registration():
    if registrationController(request.get_json()):
        return Response('', status = 200, mimetype='application/json')
    return Response('', status = 400, mimetype='application/json')

@app.route("/Api/App/login", methods=['POST'])
@cross_origin()
def login():
    result = loginController(request.get_json())
    if result: 
        data = {}
        data['token'] = result
        json_data = json.dumps(data)
        return Response(json_data, status = 200, mimetype='application/json')
    return Response('', status = 400, mimetype='application/json')

if __name__ == "__main__":
    app.run()