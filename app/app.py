from flask import Flask, jsonify, Response
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "2.0")
request_count = 0

@app.route("/")
def home():
    global request_count
    request_count += 1
    return jsonify({
        "message": "DevOps Simulation Running",
        "version": VERSION
    })

@app.route("/health")
def health():
    global request_count
    request_count += 1
    return jsonify({
        "status": "healthy"
    })

@app.route("/version")
def version():
    global request_count
    request_count += 1
    return jsonify({
        "version": VERSION
    })

@app.route("/metrics")
def metrics():
    global request_count
    metrics_output = f'app_requests_total {request_count}\n'
    return Response(metrics_output, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)