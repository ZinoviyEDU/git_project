from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__, static_folder='/home/litosh/Hillel/hw10/static')


@app.route('/')
def index():
    return redirect(url_for('main'))


@app.route("/main/")
def main():
    lst = ['Достижения Васи Пупкина', 'О Васе Пупкине', 'Связаться с Васей Пупкиным']
    color = ['red', 'blue', 'purple', 'magenta', 'black']
    with open('help.csv', mode='r') as file:
        csv = file.readlines()
        lst_csv = []
        for line in csv:
            line = line.split(',')
            lst_csv.append(line)

    output = render_template('main.html', lst=lst, lst_csv=lst_csv, name='Достижения Васи Пупкина', color=color)
    return output


@app.route('/about/')
def about():
    color = ['red', 'blue', 'purple', 'magenta', 'black']
    image = ['de-1200x675.jpg', 'index.jpeg']
    lst = ['Достижения Васи Пупкина', 'О Васе Пупкине', 'Связаться с Васей Пупкиным']
    output = render_template('about.html', name='О Васе Пупкине', lst=lst, color=color, image=image)
    return output


@app.route('/contact/')
def contact():
    color = ['red', 'blue', 'purple', 'magenta', 'black']
    option = ['option 1', 'option 2', 'option 3', 'option 4']
    lst = ['Достижения Васи Пупкина', 'О Васе Пупкине', 'Связаться с Васей Пупкиным']
    output = render_template('contact.html', name='Связаться с Васей Пупкиным', lst=lst, option=option, color=color)
    return output


@app.errorhandler(404)
def not_found(error):
    return render_template('404.htm'), 404


@app.errorhandler(500)
def idk(error):
    return render_template('500.html'), 500
