import RPi.GPIO as GPIO

def isPressed(btn, led):
    if GPIO.input(btn) == False:
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)

button1 = 3
button2 = 4
led1 = 14
led2 = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

try:
    while True:
        isPressed(button1, led1)
        isPressed(button2, led2)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')

#
#(3-7) Создаём функцию с именем isPressed. Говорим, что она принимает 2 параметра: пин кнопки и пин светодиода. В теле функции пишем условие if ... else ... для управления освещением.
#(22,23) В цикле while вызываем функцию isPressed и передаём пары кнопка-светодиод.
#