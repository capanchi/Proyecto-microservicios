from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

MS2_URL = os.getenv("MS2_URL", "http://ms2-data:8080/data")
EXTERNAL_URL = "https://www.binaria.com.ec"

@app.route("/")
def hello():
    ms2_response = requests.get(MS2_URL).json()
    external_response = requests.post(EXTERNAL_URL, json={"mensaje": "Hola desde ms1"}).json()
    return jsonify({
        "message": "Hola Mundo desde MS1",
        "ms2_response": ms2_response,
        "external_post_response": external_response
    })

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
