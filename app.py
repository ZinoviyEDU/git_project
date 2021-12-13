from os import environ
from werkzeug.exceptions import HTTPException
import json
from flask import Flask
from flask import request
from flask import render_template
import csv

app = Flask(__name__)
environ.get('.env')


@app.route("/")
@app.route("/index")
def index():
    nav = [" ", "about", "contact", 'Главная-Достижения', 'Все о Васе', 'Контакты']
    path = 'static/csv/data.csv'
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for i in reader:
            data.append({'#': i['#'], 'Дата': i['Дата'], 'Количество пройденых шагов': i['Количество пройденых шагов'],
                         'Время проведенное в спортивном зале': i['Время проведенное в спортивном зале']})
    output = render_template('index.html', title='Главная - Достижения', navigation=nav,
                             description='Достижения Васи Пупкина',
                             points=data, navi=nav)
    return output


@app.route("/about")
def about():
    nav = ["index", " ", "contact", 'Главная-Достижения', 'Все о Васе', 'Контакты']
    with open('static/txt/description.txt', 'r') as text:
        line = text.readline()
    output = render_template('about.html', title='Все о Васе', navi=nav, puth='jpg/pupkin.jpg',
                             alt="Здесь должна быть фотография Пупкина", txt=line,
                             description='Так кто же он такой, знаменитый Вася Пупкин?')
    return output


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    path = 'static/txt/data_save.txt'
    nav = ["index", "about", " ", 'Главная-Достижения', 'Все о Васе', 'Контакты']
    output = render_template('contact.html', title='Контакты', navi=nav, description='Связаться с Васей Пупкиным')
    if request.method == "GET":
        return output
    else:
        last_name = request.form.get('lastname')
        first_name = request.form.get('firstname')
        email = request.form.get('email')
        msg = request.form.get('user_message')
        with open(path, 'w') as w:
            w.write(f'Фамилия = {last_name} Имя = {first_name}, email = {email}, Сообщение {msg}')
        return output


@app.errorhandler(HTTPException)
def handle_exception(e):
    output = e.description
    if e.code == 404:
        output = render_template('404.html'), e.code
    elif e.code == 500:
        output = render_template('500.html'), e.code
    return output
