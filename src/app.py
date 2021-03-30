from flask_jsonpify import jsonpify
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})

@app.route("/getdata",methods=['GET','POST'])
def getdata():
    response =  jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    app.run()

