from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def add():
    return """<p>Человечество вырастает из детства.</p>
        <p>Человечеству мала одна планета.</p>
        <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
        <p>И начнем с Марса!</p>
        <p>Присоединяйся!</p>"""


@app.route('/image_mars')
def third_num():
    return f"""<html>
    <head><tile>Привет, Марс!</tile></head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/MARS.png')}" alt="здесь должна была быть картинка, но не нашлась">
    <p>Вот она какая, красная планета</p>
    </body></html>"""


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')