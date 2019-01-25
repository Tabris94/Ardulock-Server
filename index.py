from flask import Flask, request 
from flask_cors import cross_origin
from flask import Response
import json
from mongoengine import *
from controllers.Api_Arduino.arduino import Arduino
from controllers.Api_App.registration import registrationController
from controllers.Api_App.login import loginController
from controllers.Api_App.getArdulocks import getArdulocksController
from controllers.Api_App.setStatus import setStatusContoller
from controllers.Api_App.getLog import getLogs
from models.Users import *
from models.Devices import *

app = Flask(__name__)
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

@app.route("/Api/App/getArdulocks", methods=['POST'])
@cross_origin()
def getArdulocks():
    result = getArdulocksController(request.get_json())
    if result == 401:
        return Response('', status = 401, mimetype='application/json')
    elif result == 400:
        return Response('', status = 200, mimetype='application/json')
    else:
        data = {}
        data['mat'] = result.mat
        data['statusFirstSensor'] = result.statusFirstSensor
        data['statusSecondSensor'] = result.statusSecondSensor
        data['labelFirstSensor'] = result.labelFirstSensor
        data['labelSecondSensor'] = result.labelSecondSensor
        json_data = json.dumps(data)
        return Response(json_data, status = 200, mimetype='application/json')

@app.route("/Api/App/setStatus", methods=['POST'])
@cross_origin()
def setStatus():
    return Response('', status = setStatusContoller(request.get_json()), mimetype='application/json')

@app.route("/Api/App/getLog", methods=['POST'])
@cross_origin()
def getLog():
    result = getLogs(request.get_json())
    data={}
    row={}
    i=-1
    for x in result:
        i+=1
        data[i]= x.txt + x.time.strftime(' %d/%b/%Y alle %H:%M')

    json_data= json.dumps(data)
    return Response(json_data, status = 200, mimetype='application/json')

if __name__ == "__main__":
    app.run()