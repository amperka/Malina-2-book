from flask import Flask, send_file
from flask_socketio import SocketIO
import RPi.GPIO as GPIO

app = Flask('feedback')
socketio = SocketIO(app)

btn = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN)


@app.route('/')
def index():
    return send_file('feedback.html')


@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)


@socketio.on('isPressed')
def checkButton(receivedData):
    if GPIO.input(btn) == False:
        socketio.emit('button', 'pressed')
    else:
        socketio.emit('button', 'released')


try:
    socketio.run(app, port=3000, host='0.0.0.0')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')
