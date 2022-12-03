import imp
import multiprocessing
from flask import Flask, request, jsonify
from uuid import uuid4
import threading
import datetime
from hashlib import sha256
import base64

host_name = "0.0.0.0"
port = 1006

app = Flask(__name__)

_requests_queue: multiprocessing.Queue = None

@app.route("/get_gps")
def get_gps():
    return "ok"

def start_rest(requests_queue):
    global _requests_queue 
    _requests_queue = requests_queue
    threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()

if __name__ == "__main__":        # on running python app.py
    start_rest()