from flask import Flask
from mongoengine import *
from models.Devices import Devices
from models.Users import Users
from models.Logs import Logs

app = Flask(__name__)
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/ArduLock'
app.debug = True

connect('Ardulock-db', host='localhost', port=27017)

@app.route("/")
def add():
    result = Devices( 
        mat = 'TEST3',
        statusFirstSensor = True,
        statusSecondSensor = False,
        last_EndPoint = 'asdasda',  
    ) 
    result.save()
    return 'hello world'
    
@app.route("/1")
def first():
    result = Users(
        email = 'andrea.cipollaro.94@gmail.com',
        first_name = 'andrea',
        last_name = 'cipollaro',
        password = 'arduino29',
        token = '',
    )
    result.save()
    return "first"

@app.route("/2")
def second():
    return  "second"

if __name__ == "__main__":
    app.run()