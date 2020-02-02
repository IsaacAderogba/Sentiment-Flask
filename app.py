from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api", methods=["GET"])
def get_api_status():
    return "Api v1"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
