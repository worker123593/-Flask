from flask import Flask, url_for, request

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


@app.route('/promotion_image')
def fourth_num():
    return f"""<html>
    <head>
        <tile>Привет, Марс!</tile>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    </head>
    <body>
    <h1 class="red">Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/MARS.png')}" alt="здесь должна была быть картинка, но не нашлась">
    <p class="alert alert-secondary" role="alert">Человечество вырастает из детства.</p>
    <p class="alert alert-primary" role="alert">Человечеству мала одна планета.</p>
    <p class="alert alert-warning" role="alert"> Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="alert alert-success" role="alert">И начнем с Марса!</p>
    <p class="alert alert-danger" role="alert">Присоединяйся!</p>
    </body></html>"""


@app.route('/astronaut_selection', methods=["GET", "POST"])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"
                             /> <title>Пример формы</title> </head>
                              <body>
                               <div class='center'> <h1>Анкета претендента</h1> <h2>  на участие в миссии</h2> 
                              <form class="login_form" method="post"><input type="text" class="form-control"
                               id="surname" placeholder="Введите фамилию" name="surname"> 
                               <input type="text" class="form-control" id="name"
                                placeholder="Введите имя" name="name"> <br> <input type="email" class="form-control" 
                                id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email"> 
                                <div class="form-group"> <label for="classSelect">Какое у Вас образование?</label> 
                                <select class="form-control" id="classSelect" name="class"> <option>Начальное</option> 
                                <option>Среднее</option> <option>Высшее</option> </select> </div> 
                                        
                                        <div class="form-group"> <label>Какие у Вас есть профессии?</label> <div 
                                        class="form-check"> <input type="checkbox" class="form-check-input" 
                                        id="acceptRules1" name="accept1"> <label class="form-check-label" 
                                        for="acceptRules1">Пилот</label> </div> <div class="form-check"> <input 
                                        type="checkbox" class="form-check-input " id="acceptRules2" name="accept2"> 
                                        <label class="form-check-label" for="acceptRules2">Метеоролог</label> </div> 
                                        <div class="form-check"> <input type="checkbox" class="form-check-input " 
                                        id="acceptRules3" name="accept3"> <label class="form-check-label" 
                                        for="acceptRules3">Экзобиолог</label> </div> <div class="form-check"> <input 
                                        type="checkbox" class="form-check-input " id="acceptRules4" name="accept4"> 
                                        <label class="form-check-label" for="acceptRules4">Врач</label> </div> <div 
                                        class="form-check"> <input type="checkbox" class="form-check-input " 
                                        id="acceptRules5" name="accept5"> <label class="form-check-label" 
                                        for="acceptRules5">Инженер</label> </div> </div> 
                                        <div class="form-group"> <label for="form-check">Укажите пол</label> <div 
                                        class="form-check"> <input class="form-check-input" type="radio" name="sex" 
                                        id="male" value="male" checked> <label class="form-check-label" 
                                        for="male">Мужской</label> </div> <div class="form-check"> <input 
                                        class="form-check-input" type="radio" name="sex" id="female" value="female"> 
                                        <label class="form-check-label" for="female">Женский</label> </div> </div> 
                                        <div class="form-group"> <label for="about">Почему Вы хотите принять участие 
                                        в миссии?</label> <textarea class="form-control" id="about" rows="3" 
                                        name="reazon"></textarea> </div> 
                                        
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input class="form-check-input" type="checkbox" name="degree" id="degree">
                                            <label for="degree" class=form-check-label>Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                            </body></html>'''
    elif request.method == 'POST':
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        #     print(request.form.get('sex'))
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
