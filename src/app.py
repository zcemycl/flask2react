from flask_jsonpify import jsonpify
from flask import Flask, request, stream_with_context, Response
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})

@app.route("/getdata",methods=['GET','POST'])
def getdata():
    data = random.randint(1,10)
    response = jsonpify({'output':'Hello Leo','data':data})
    return response

if __name__ == "__main__":
    app.run()

