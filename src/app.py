from flask_jsonpify import jsonpify
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonpify({'output':'Hello World','data':[10,2,8,5,6,1]})

if __name__ == "__main__":
    app.run()

