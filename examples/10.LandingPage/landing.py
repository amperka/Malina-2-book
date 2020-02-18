from flask import Flask, send_file

app = Flask('landingPage')


@app.route('/')
def index():
    return send_file('landing.html')


@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)


app.run(port=3000, host='0.0.0.0')
