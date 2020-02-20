import RPi.GPIO as GPIO

def isPressed(btn, led):
    state = 1 - GPIO.input(btn)
    GPIO.output(led, state)

leds = [12, 13, 14, 18]
buttons = [2, 3, 4, 8]

GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(leds[i], GPIO.OUT)
    GPIO.setup(buttons[i], GPIO.IN)

try:
    while True:
        for i in range(4):
            isPressed(buttons[i], leds[i])
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')

#
#(4) GPIO.input() возвращает либо 0 либо 1. Вычитаем из единицы значение, получаем обратное.
#(11) Функция range(n) создаёт диапазон от 0 до n для перебора в цикле for. Число 4 равно длине массивов кнопок и светодиодов.
#