from flask_jsonpify import jsonpify
from flask import Flask, request, stream_with_context, Response, render_template
from flask_cors import CORS
import random
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
CORS(app)
socketio = SocketIO(app,cors_allowed_origins='*')
#CORS(socketio)

@app.route("/")
def home():
    return jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})

@app.route("/getdata",methods=['GET','POST'])
def getdata():
    data = random.randint(1,10)
    response = jsonpify({'output':'Hello Leo','data':data})
    return response

@app.route("/session", methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived, broadcast=True)


if __name__ == "__main__":
    socketio.run(app,debug=True)

