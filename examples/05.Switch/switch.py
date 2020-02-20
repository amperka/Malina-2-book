import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

try:
    while True:
        button = GPIO.input(8)
        if button == False:
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
        else:
            GPIO.output(24, GPIO.LOW)
            GPIO.output(26, GPIO.HIGH)
            
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')

#
#(4-6) Настраиваем один пин на вход для кнопки, а два других на выход для светодиодов.
#(12-13) Если значение переменной button равно False (кнопка нажата), включаем светодиод 24 и выключаем светодиод 26.
#(15-16) Ветвь «иначе». Если button не равно False, включаем светодиод 26 и выключаем 24.
#
