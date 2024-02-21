from flask import Flask
import socketio

sio = socketio.Client() 

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hola</h1>"