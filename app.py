from datetime import date
from flask import Flask, url_for, request
from flask import render_template
from flask.cli import load_dotenv
from werkzeug.utils import redirect

app = Flask(__name__)
app.run(debug=True)
load_dotenv('.env')


@app.route('/')
def main():
    return redirect(url_for('index'))


@app.route("/index")
def index():
    title_dict = {
        'title': 'Главная - Достижения Васи Пупкина',
        'keywords': 'таблица достижений, достижения, спорт, Вася, Пупкин, количество шагов',
        'description': 'Таблица достижений Васи Пупкина, которых он достиг благодаря своей '
                       'уникальной силе воли'
    }
    table_of_achievements = {
        '#': [i for i in range(1, 14)],
        'Дата': [str(date.fromordinal(i)) for i in
                 [d for d in range(date(year=2020, month=11, day=20).toordinal(),
                                   date(year=2020, month=12, day=3).toordinal())]],
        'Количество пройденных шагов': ['7403', '3453', '4539', '11940', '6373', '1409', '5549',
                                        '7429', '7302', '6201', '4958', '7603', '6967'],
        'Время проведенное в спортивном зале': ['2 часа 43 минуты', 'Не посещал',
                                                'Не посещал', 'Не посещал', '2 часа 16 минут',
                                                'Не посещал', 'Не посещал', '1 час 21 минута',
                                                'Не посещал', '1 час 51 минута', 'Не посещал',
                                                'Не посещал', 'Не посещал']
    }
    output = render_template('index.html', title=title_dict, table=dict(table_of_achievements))
    return output


@app.route('/about')
def about():
    title_dict = {
        'title': 'Обо мне любимом ',
        'keywords': 'биография, история, Вася Пупкин',
        'description': 'Рассказ о человеке Васе Пупкине и его необычным достижениям'}
    about_dict = {
        'image': '/static/image/Channing_Tatum.png',
        'text': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                "when an unknown printer took a galley of type and scrambled it to make a "
                "type specimen book. It has survived not only five centuries, but also the leap "
                "into electronic typesetting, remaining essentially unchanged. It was popularised "
                "in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                "and more recently with desktop publishing software like Aldus PageMaker including "
                "versions of Lorem Ipsum."
    }
    output = render_template('about.html', title=title_dict, about=about_dict)
    return output


@app.route('/contact', methods=["GET", "POST"])
def contact():
    title_dict = {
        'title': 'Связаться с Васей Пупкиным',
        'keywords': 'контакты, связаться, связь, написать, email',
        'description': 'Для связи Вася Пупкин использует email, '
                       'поэтому можете смело писать и не переживать, что ваше письмо некто не увидит'
    }
    theme_options = {
        'select': 'Выберите тему сообщения',
        'option1': 'Предложение',
        'option2': 'Пожелание',
        'option3': 'Поздравление',
        'option4': 'Вопрос'
    }
    if request.method == 'POST':
        form = {}
        first_name = request.form['first_name']
        form.update({'first_name': first_name})
        last_name = request.form['last_name']
        form.update({'last_name': last_name})
        email = request.form['email']
        form.update({'email': email})
        theme = request.form['theme']
        form.update({'theme': theme})
        message = request.form['message']
        form.update({'message': message})
        reply = request.form.get('reply')
        form.update({'reply': reply})
        write_form(form)
        return render_template("contact.html", option=theme_options, title=title_dict)
    else:
        if request.method == 'GET':
            return render_template("contact.html", option=theme_options, title=title_dict)


def write_form(text):
    with open('form.txt', 'a') as f:
        f.write(str(text) + '\n')


@app.errorhandler(404)
def page_not_found(e):
    title_dict = {
        'title': 'Dude, you made a mistake entering the URL',
        'keywords': 'error, 404',
        'description': 'Error 404'
    }
    content_dict = {'image': '/static/image/error-404.jpg'}
    return render_template('404.html', title=title_dict, content=content_dict), 404


@app.errorhandler(500)
def exception_handler(e):
    title_dict = {
        'title': 'Wow, this is a server error!',
        'keywords': 'error, 500',
        'description': 'Error 500'
    }
    content_dict = {'image': '/static/image/500.jpeg'}
    return render_template('500.html', title=title_dict, content=content_dict), 500
