import time
import vk_api

vk = vk_api.VkApi(token='твой_ключ')

param = {
    'count': 1,
    'time_offset': 5,
    'filter': 'unread'
}

def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id': random
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
            write_msg(my_id, text, random)
        time.sleep(1)
except KeyboardInterrupt:
    print('Keyboard interrupt detected.')
finally:
    print('The program was stopped.')

#
#(4) Инициализируем бота. Вместо твой_ключ следует подставить строку с ключом доступа приложения, который тебе присвоил ВКонтакте.
#(6-9) Словарь param хранит параметры запроса: сколько присылать сообщений за раз (1), за какой период (5 секунд) и только непрочитанные.
#(12-16) Создаём функцию отправки сообщений указанным пользователям user_id с заданным текстом msg. Уникальный идентификатор random предотвращает повторную отправку одинаковых сообщений.
#(21) Раз в секунду отправляем запрос серверу ВКонтакте.
#(22-29) Если есть новые сообщения – сохраняем id отправителя, текст сообщения, уникальный идентификатор и передаем их в функцию отправки сообщений.
#