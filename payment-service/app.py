from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods = ["GET"])

def health():
    return jsonify({
        "service" : "user-service",
        "status": "healthy"}), 200

if __name__ == '__main__':
    app.run(port = 5003, debug = True)