import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [12, 13, 14, 18]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)

time.sleep(3)

for led in leds:
    GPIO.output(led, GPIO.LOW)

GPIO.cleanup()

#
#(5) Создаём массив светодиодов.
#(7) В цикле for настраиваем пины светодиодов на режим цифрового выхода и сразу включаем их.
#(13) Через 3 секунды после включения гасим светодиоды.
#(16) Освобождаем пины от управления программой.
#