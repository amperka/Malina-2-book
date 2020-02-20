from flask import Flask, send_file
import RPi.GPIO as GPIO

led = 18

GPIO.setmode(GPIO.BGM)
GPIO.setup(led, GPIO.OUT)

app = Flask('lightControl')

@app.route('/')
def index():
    return send_file('light.html')

@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)

@app.route('/turnOn')
def index():
	GPIO.output(led, GPIO.HIGH)
    return 'turnedOn'

@app.route('/turnOff')
def index():
	GPIO.output(led, GPIO.LOW)
    return 'turnedOff'

try:
	app.run(port=3000, host='0.0.0.0')
finally:
	GPIO.cleanup()
	print('GPIO cleanup completed.')

#
#(4-7) Настраиваем пин 18 на работу со светодиодом.
#(11-13) Отдаём клиенту страницу с кнопкой light.html.
#(19-27) При запросе клиента turnOff или turnOn вызываем соответствующий обработчик.
#(29-33) {sign Lighting} ВАЖНО! Обработка исключения except KeyboardInterrupt здесь не нужна, так как она уже реализована внутри Flask.
#
