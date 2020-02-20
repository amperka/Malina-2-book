import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 1000)
dutyCycle = 50
pwm.start(dutyCycle)

try:
    while True:
        time.sleep(0.01)
        dutyCycle = dutyCycle + 1
        if (dutyCycle > 100):
            dutyCycle = 0
        pwm.ChangeDutyCycle(dutyCycle)

except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')

#
#(6) Пин 18 будет работать в режиме ШИМ на частоте 1000 герц.
#(7) Запускаем ШИМ на пине с коэффициентом заполнения 50%, это зажжёт светодиод вполсилы.
#(13) На каждой итерации цикла увеличиваем значение переменной на 1.
#(14-15) Коэффициент заполнения принимает значения от 0 до 100. Если вышли за допустимые границы, обнуляем значение.
#(16) Обновляем коэффициент заполнения новым значением dutyCycle.
#