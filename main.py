from flask import Flask
from faker import Faker
import requests
from base58 import b58decode, b58encode


app = Flask(__name__)
faker = Faker()


@app.route('/')
def test_hw():
    return "<p><a href='/requirements/'>Task 1</a></p>" \
           "<p><a href='/generate-users/5'>Task 2</a></p>" \
           "<p><a href='/mean/'>Task 3</a></p>" \
           "<p><a href='/space/'>Task 4</a></p>" \
           "<p><a href='/base58encode/1234'>Task 5</a></p>" \
           "<p><a href='/base58encode/2j'>Task 6</a></p>"


@app.route("/requirements/")
def read_req():
    li = ''
    with open('requirements.txt', 'r') as file:
        for i in file:
            li += i
        return f'<pre>{li}</pre>'


@app.route("/generate-users/<int:xx>")
def gen_fake(xx):
    di = {}
    for i in range(xx):
        di.update({faker.name(): faker.free_email()})
    return di


def av(csv):
    f = open(csv, "r")
    f_line = f.readlines()[1:]
    l_count = 0
    h = 0.0
    w = 0.0
    for i in f_line:
        try:
            i = i.split(',')
            h += float(i[1])
            w += float(i[2])
            l_count += 1
        except IndexError:
            pass
    m_h = round((h / l_count) * 2.54, 2)
    m_w = round((w / l_count) * 0.45, 2)
    return f'<pre>Parsed file:{csv}\n' \
           f'Total values in file (strings of data):{l_count}\n' \
           f'Average height:{m_h}cm\n' \
           f'Average weight:{m_w}kg</pre>'


@app.route("/mean/")
def mean():
    return av("hw05.csv")


@app.route("/space/")
def men_in_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()


@app.route("/base58encode/<string:s_string>")
def code_to_base58(s_string):
    return b58encode(s_string)


@app.route("/base58encode/<string:s_string>")
def base58_to_str(s_string):
    return b58decode(s_string)
