# About project...03_01_2022
STARTED WORK WITH FLASK_part_1:

task_0
# before starting to work with the flask, I need to install and import some library (step by step)

from flask import Flask
from faker import Faker
from mimesis import Person
import csv
import requests
import base58
from markupsafe import escape

app = Flask(__name__)
# all @app.route() must end --> app.run(debug=True) -->or one time at the end of the document

#Общие рекомендации:

 - используйте в работе линтер flake8 или аналогичный
 - добавьте в проект файл README.md с описанием процесса запуска вашего приложения
 - весь функционал можно реализовать в одном файле app.py
 - используйте в работе Git и файл .gitignore
 - пользуйтесь виртуальными окружениями и создайте файл requirements.txt
 - если выводите текст в качестве ответа браузеру, то его можно обернуть в тег <pre> для корректного отображения пробелов и переносов строк
 - постарайтесь, хоть по-минимуму обрабатывать возможные ошибки
#В качестве результата размещайте ссылку на PR

# Go!Go!Go!Go!Go!

task_1
 - essence of the task:
         Возвращать содержимое файла с Python пакетами (requirements.txt)
         PATH: /requirements/
         Фактически необходимо открыть файл requirements.txt и вернуть его содержимое

- decision of the task:
# task_1 Return the contents of a file with Python packages(used requirements.txt)

@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as f:
        return f'<pre> {f.read()}</pre>'

- result of the task:
                 certifi==2021.10.8
                 charset-normalizer==2.0.8
                 idna==3.3
                 requests==2.26.0
                 urllib3==1.26.7

task_2
- essence of the task:
                Вывести `XX` случайно сгенерированных пользователей (имя и почту)
                Например: Dmytro aasdasda@mail.com
                PATH: /generate-users/XX
                где XX - параметр который регулирует количество пользователей (тип `int`)
                Для генерации пользователей можно воспользоваться библиотекой Faker
- decision of the task:
# task_2 Print `XX` for randomly generated users (name and email) (used the Faker library --> showed result: Kristin Rodriguez stephaniepierce@example.com)
# ??? - didn't find how to apply the first name

@app.route('/generate-users/<int:info>')
def generate_users(info):
    fake = Faker()
    data = ''
    for _ in range(info):
        data += f'{fake.name()} {fake.email()}\n'
    return f'<pre>{data}</pre>'


# task_2.1 (used the Mimesis library --> showed result: Reatha researchers1898@live.com)

@app.route('/generate-users_2/<int:info>')
def generate_users_2(info):
    person = Person()
    data = ''
    for _ in range(info):
        data += f'{person.name()} {person.email()}\n'
    return f'<pre>{data}</pre>'

- result of the task_2:
                    Robert Gray austin43@example.net
                    Alejandro Smith christopher50@example.org
                    Victoria Lee katherinelivingston@example.com
                    Colton Murphy denise61@example.org
                    Karla Dean benjamin74@example.net
- result of the task_2.1:
                    Suellen dec2004@live.com
                    Kenny tmp2045@gmail.com
                    Keenan dns1917@protonmail.com
                    Kendrick connecting1875@yandex.com
                    Mireille seconds1893@yahoo.com
task_3
- essence of the task:
          Обработать файл CSV и вернуть результат
           Вернуть значения среднего роста (в сантиметрах) и среднего веса (в килограммах)
          Необходимые данные расположены в файле hw05.csv
          Анализировать файл hw.csv нужно при каждом вызове
          PATH: /mean/
          Пример возвращаемого результата (где XX - соответствующие значения):
           Parsed file: XX
          Total values in file (strings of data): XX
           Average height: XX cm
           Average weight: XX kg
- decision of the task:
# task_3 Process the CSV file and return the result (average of height and weight, used file hm05.csv)

@app.route('/mean/')
def ave():
    inches_to_cm = 2.54
    pounds_to_kg = 0.453592

    with open('hw05.csv', 'r', newline='') as count_file:
        csv_reader = csv.DictReader(count_file)
        sum_height = 0
        sum_weight = 0
        string_count = 0

        for row in csv_reader:
            height = row.get(' "Height(Inches)"')
            weight = row.get(' "Weight(Pounds)"')
            sum_height += float(height)
            sum_weight += float(weight)
            string_count += 1

    # found the average in inches, pounds

    avg_height = sum_height / string_count
    avg_weight = sum_weight / string_count

    # display values to_cm, to_kg

    Average_height = round(avg_height * inches_to_cm)
    Average_weight = round(avg_weight * pounds_to_kg)

    # ?  how do i display Parsed file: 1- manual(by hands), 2 - variable

    return f'<pre> Parsed file: hw05.csv </pre> ' \
           f'<pre> Line count = {string_count + 1}</pre> ' \
           f'<pre> Line count(strings of data) = {string_count}</pre>' \
           f'<pre> Average height:  {Average_height} cm </pre>' \
           f'<pre> Average weight:  {Average_weight} kg </pre>'
- result of the task:
              Parsed file: hw05.csv 
              Line count = 25001
              Line count(strings of data) = 25000
              Average height:  173 cm 
              Average weight:  58 kg 

task_4
- essence of the task:
                  Вывести количество космонавтов, находящихся в настоящий момент на орбите
                  Получить информацию о космонавтах можно тут
                  Для получения данных можно воспользоваться библиотекой requests
                  PATH: /space/
                  Пример работы с библиотекой requests, вначале необходимо установить библиотеку командой:
                  $ pip install requests
                  Пример:
                  import requests
                  r = requests.get('https://api.github.com/repos/psf/requests')
                  r.json()["description"]
- decision of the task:
# task_4 Display the number of astronauts currently in orbit

# http://api.open-notify.org/astros.json --> astronaut data
# https://pythonhosted.org/Flask-JSON/ --> decision

@app.route('/space/')
def qty_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    return f'<pre> Number of astronauts: {r["number"]}</pre>'

- result of the task:
                     Number of astronauts: 10

task_5
- essence of the task:
                      Закодировать входную строку `STRING` в формате base58
                      Входная строка должна быть без пробелов
                      PATH: /base58encode/STRING
                      где STRING - это строка, которую необходимо закодировать в формате base58
                      Для работы с кодированием base58 можно использовать одноименную библиотеку base58 ($ pip install base58)
                      Обшая информация о кодировании base58
- decision of the task:
# task_5 Encode input string `STRING` in base58 format -->($ pip install base58)-->used the base58 library

# https://ru.wikipedia.org/wiki/Base58 --> General information about base58 encoding
# https://www.programcreek.com/python/example/98799/base58.b58encode -->example
# https://pypi.org/project/base58/

# ? didn't sure--> this is the result - correct

@app.route('/base58encode/<string>')
def b58_encode(string):
    st = base58.b58encode(string).decode('utf-8')  # ?  .decode(utf-8)
    return f'<pre>Encode input string: {string} in base58 format --> {st}</pre>'

- result of the task:
                    Encode input string: requirements in base58 format --> 3AD4Cc1hKxhyTwxhQ

task_6
- essence of the task:
                     Преобразовать строку `STRING_IN_BASE58` в формате *base58* в исходную строку
                     PATH: /base58decode/STRING_IN_BASE58`
                     где STRING_IN_BASE58 - это строка, которую необходимо преобразовать из формата base58 в исходную строку
                     Для работы с кодированием base58 можно использовать библиотеку base58
                     Фактически, можно себя проверить (протестировать). Подать на вход обработчика /base58encode/ строку, а полученный результат передать в /base58decode/. При этом полученный на выходе второго обработчика результат должен совпасть с исходной строкой
- decision of the task:
# task_6 Convert string `STRING_IN_BASE58` in base58  format to original string

@app.route('/base58decode/<STRING_IN_BASE58>')
def b58_decode(STRING_IN_BASE58):
    st = base58.b58decode(STRING_IN_BASE58).decode('utf-8')  # ?  .decode(utf-8)
    return f'<pre>Decode input string: {STRING_IN_BASE58} in base58 format to original string --> {st}</pre>'

- result of the task:
                    Decode input string: 3AD4Cc1hKxhyTwxhQ in base58 format to original string --> requirements

#FINISH...