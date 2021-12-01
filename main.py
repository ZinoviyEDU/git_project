from flask import Flask
from faker import Faker
from markupsafe import escape
import requests
import base58


fake = Faker()
app = Flask(__name__)


@app.route("/")
def hello():
    return"<p><a href='/requirements/'>Task 1</a></p>"\
           "<p><a href='/generate-users/12'>Task 2</a></p>" \
           "<p><a href='/mean/'>Task 3</a></p>" \
           "<p><a href='/space/'>Task 4</a></p>" \
           "<p>/base58encode/(some_text_here)</p>" \
           "<p>/base58decode/5ziMaBDbffsXdFoZEpM7Ep</p>"





@app.route("/requirements/")
def send_requirements():
    f = open('requirements.txt', 'r')
    string = ''
    for item in f:
        string = string + item
    f.close()
    return f'<pre>{string}</pre>'


@app.route('/generate-users/<int:XX>')
def show_post(XX):
    dictionary = {}
    for item in range(XX):
        name = fake.name()
        address = fake.email()
        x = {name: address}
        dictionary.update(x)
    return dictionary


@app.route('/mean/')
def start_mean():
    return mean_value('hw05.csv')


def mean_value(file_path):
    with open(file_path, mode='r') as file:
        csv = file.readlines()[1:]
        height = 0.0
        weight = 0.0
        lst = []
        count = 0
        for line in csv:
            line = line.split(',')
            for item in line:
                lst.append(float(item))
            height = height + (lst[1]*2.58)
            weight = weight + (lst[2]*2.205)
            lst = []
            count += 1

        mean_height = height / count
        mean_weight = weight / count
        return f'<pre>Parsed file:{file_path}\n' \
               f'Total values in file (strings of data):{count}\n' \
               f'Average height:{mean_height}sm\n' \
               f'Average weight:{mean_weight}kg</pre>'


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()


@app.route('/base58encode/<STRING>')
def base58encode(STRING):
    return base58.b58encode(STRING)


@app.route('/base58decode/<STRING_IN_BASE58>')
def base58decode(STRING_IN_BASE58):
    return base58.b58decode(STRING_IN_BASE58)

