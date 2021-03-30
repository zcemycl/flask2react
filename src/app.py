from flask_jsonpify import jsonpify
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})

@app.route("/getdata",methods=['GET','POST'])
def getdata():
    response =  jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})
    return response

if __name__ == "__main__":
    app.run()

