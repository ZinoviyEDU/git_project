from flask import Flask
from faker import Faker
from mimesis import Person
import csv
import requests
import base58

from markupsafe import escape

app = Flask(__name__)


# task_1 Return the contents of a file with Python packages(used requirements.txt)

@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as f:
        return f'<pre> {f.read()}</pre>'


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


# task_4 Display the number of astronauts currently in orbit

# http://api.open-notify.org/astros.json --> astronaut data
# https://pythonhosted.org/Flask-JSON/ --> decision

@app.route('/space/')
def qty_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    return f'<pre> Number of astronauts: {r["number"]}</pre>'


# task_5 Encode input string `STRING` in base58 format -->($ pip install base58)-->used the base58 library

# https://ru.wikipedia.org/wiki/Base58 --> General information about base58 encoding
# https://www.programcreek.com/python/example/98799/base58.b58encode -->example
# https://pypi.org/project/base58/

# ? didn't sure--> this is the result - correct

@app.route('/base58encode/<string>')
def b58_encode(string):
    st = base58.b58encode(string).decode('utf-8')  # ?  .decode(utf-8)
    return f'<pre>Encode input string: {string} in base58 format --> {st}</pre>'


# task_6 Convert string `STRING_IN_BASE58` in base58  format to original string

@app.route('/base58decode/<STRING_IN_BASE58>')
def b58_decode(STRING_IN_BASE58):
    st = base58.b58decode(STRING_IN_BASE58).decode('utf-8')  # ?  .decode(utf-8)
    return f'<pre>Decode input string: {STRING_IN_BASE58} in base58 format to original string --> {st}</pre>'

app.run(debug=True)
