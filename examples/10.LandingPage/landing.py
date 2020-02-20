from flask import Flask, send_file

app = Flask('landingPage')

@app.route('/')
def index():
    return send_file('landing.html')

@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)

app.run(port=3000, host='0.0.0.0')

#
#(1) Дополнительно к функции Flask подключаем функцию send_file .
#(7) Возвращаем web-клиенту файл с html-кодом страницы.
#(11) Добавляем обработчик запросов файлов из папки с изображениями.
#