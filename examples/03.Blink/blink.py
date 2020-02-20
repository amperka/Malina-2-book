import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        time.sleep(0.5)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(17, GPIO.LOW)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')

#
#(2) Импортируем модуль time для функции задержки времени.
#(8) Константа true всегда истинна, поэтому цикл будет выполняться вечно.
#(9) Вызываем функцию sleep из модуля time. Параметр 0.5 задаёт задержку в полсекунды.
#(13) Отлавливаем исключение сообщающее о прерывании программы клавишами ctrl+C.
#(16-17) Поместив внутрь блока finally функцию GPIO.cleanup(), можно быть уверенным, что пины Raspberry сбросятся в начальное состояние.
#