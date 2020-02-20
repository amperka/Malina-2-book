import time
import vk_api

from deluge_client import DelugeRPCClient

vk = vk_api.VkApi(token='твой_ключ')

values = {
    'count': 1,
    'time_offset': 5,
    'filter': 'unread'
}

client = DelugeRPCClient(
    '127.0.0.1',
    58846,
    'pi',
    'пароль_твоей_Raspberry'
)

client.connect()

def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id': random
    })

try:
    while True:
        response = vk.method('messages.getConversations', values)
        if response['items']:
            item = response['items'][0]
            last_mess = item['last_message']
            random = last_mess['random_id']
            my_id = last_mess['peer_id']
            text = last_mess['text']
            try:
                client.call('core.add_torrent_url', text, {
                    'download_location': '/home/pi/Torrents'
                })
            except Exception:
                write_msg(my_id, 'Link doesn\'t work', random)
            else:
                write_msg(my_id, 'Download started!', random)
        time.sleep(1)
except KeyboardInterrupt:
    print('Keyboard interrupt detected.')
finally:
    print('Program was stopped.')

#
#(4) Импортируем класс DelugeRPCClient из библиотеки deluge_client .
#(14-18) Создаём объект client для подключения к серверу deluge-web. Указываем локальный IP-адрес, порт, логин и пароль.
#(21) Подключаемся к серверу.
#(40) Функция API core.add_torrent_url принимает URL на торрент-файл и ставит его в очередь на скачивание. Дополнительно передаём параметр download_location, чтобы сохранить совместимость с deluge-web и web-пультом в хранении файлов.
#(42-45) Перехватываем исключения порожденные функцией client.call() не связанные с завершением программы. Если исключений не возникло, отправляем сообщение о начале загрузки.
#