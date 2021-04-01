from flask_jsonpify import jsonpify
from flask import Flask,request,stream_with_context,Response,render_template
from flask_cors import CORS
import random
import time
from threading import *
from flask_socketio import SocketIO,send,emit
import eventlet

eventlet.monkey_patch()
thread = Thread()
thread_stop_event = Event()
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

class RandomThread(Thread):
    def __init__(self):
        self.delay = 60
        super(RandomThread, self).__init__()
    def randomNumberGenerator(self):
        print("Making random numbers")
        while not thread_stop_event.isSet():
            number = round(random.random()*10, 3)
            #print(number)
            socketio.emit('newnumber', {'number': number}, namespace='/test')
            time.sleep(self.delay)
    def run(self):
        self.randomNumberGenerator()

@app.route("/")
def home():
    return jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})

@app.route("/getdata",methods=['GET','POST'])
def getdata():
    data = random.randint(1,10)
    response = jsonpify({'output':'Hello Leo','data':data})
    return response

@app.route('/getrealtimedata')
def index():
    return render_template('index.html')

@app.route("/session")
def session():
    return render_template('session.html')

@socketio.on('my_event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    emit('my_response',json,broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    print('Client connected')
    #if not thread.isAlive():
    print("Starting Thread")
    thread = RandomThread()
    thread.start()

if __name__ == "__main__":
    socketio.run(app,debug=True)

