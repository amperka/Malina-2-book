import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

while True:
    time.sleep(0.5)
    button = GPIO.input(2)
    print(button)

#
#(5) Настраиваем пин 2 на вход.
#(9) Функцией input считываем значение пина и записываем его в переменную button.
#
