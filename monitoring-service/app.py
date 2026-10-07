from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def check():

    responses = {
        "user" : requests.get("http://127.0.0.1:5001/health").json(),
        "product" : requests.get("http://127.0.0.1:5002/health").json(),
        "order" : requests.get("http://127.0.0.1:5003/health").json()
    }

    return jsonify(responses),200



if __name__ == '__main__':
    app.run(port = 5000, debug = True)