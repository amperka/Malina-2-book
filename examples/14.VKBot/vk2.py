import time
import vk_api
import RPi.GPIO as GPIO

vk = vk_api.VkApi(token='твой ключ')

param = {
    'count': 1,
    'time_offset': 5,
    'filter': 'unread'
}

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)


def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id': random,
    })


try:
    while True:
        response = vk.method('messages.getConversations', param)
        if response['items']:
            item = response['items'][0]
            last_mess = item['last_message']
            random = last_mess['random_id']
            my_id = last_mess['peer_id']
            text = last_mess['text']
            if text == 'On':
                GPIO.output(led, GPIO.HIGH)
                write_msg(my_id, 'LED ' + text, random)
            elif text == 'Off':
                GPIO.output(led, GPIO.LOW)
                write_msg(my_id, 'LED ' + text, random)
            else:
                err_msg = 'Send "On" or "Off"'
                write_msg(my_id, err_msg, random)
        time.sleep(1)
    GPIO.setmode(GPIO.BCM)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')
