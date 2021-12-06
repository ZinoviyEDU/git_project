from flask import Flask, jsonify, render_template, request
from markupsafe import escape
from faker import Faker
import requests
import base58
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open('data/content.csv', mode='r') as fh:
        csv_read = fh.readlines()
    res = render_template('index.html', index_content=csv_read)
    return res


# Case 1

def read_requirements(path):
    with open(path, 'r') as fh:
        all_lines = fh.read()
        return all_lines


@app.route('/requirements')
def requirements():
    data = read_requirements('requirements.txt')
    res = render_template('requirements.html', requirements=data)
    return res


# Case 2

@app.route('/generate-users/<int:number>', methods=['post', 'get'])
def generate_users(number):
    faker = Faker()
    if request.method == 'POST':
        number = int(request.form.get('count'))
        names = [[faker.unique.name(), faker.email()] for i in range(number)]
        res = render_template('fake_data.html', num=number, users_list=names)
    else:
        names = [[faker.unique.name(), faker.email()] for i in range(number)]
        res = render_template('fake_data.html', num=number, users_list=names)
    return res


# Case 3

def calculate_mean(path):
    lines_count = 0
    sum_height = 0.0
    sum_weight = 0.0
    avg_height = 0.0
    avg_weight = 0.0
    with open(path, mode='r') as fh:
        csv_read = fh.readlines()[1:]
        for line in csv_read:
            line = line.split(',')
            if len(line) > 1:
                sum_height += float(line[1])
                sum_weight += float(line[2])
                lines_count += 1
        avg_height = round((sum_height / lines_count) * 2.54, 2)
        avg_weight = round((sum_weight / lines_count) * 0.453592, 2)
        path = path.split('/')[1]
        return path, str(lines_count), str(avg_height), str(avg_weight)


@app.route('/mean')
def calculate():
    res_tup = calculate_mean('data/hw05.csv')
    res = render_template('mean.html', path=res_tup[0], lines_count=res_tup[1], avg_height=res_tup[2],
                          avg_weight=res_tup[3])
    return res


# Case 4

@app.route('/space')
def space():
    req = requests.get('http://api.open-notify.org/astros.json')
    space_bums = req.json()['people']
    res = render_template('space.html', bums=space_bums)
    return res


# Case 5

@app.route('/base58encode', methods=['post', 'get'])
def encoder():
    if request.method == 'GET':
        res = render_template('base58encode.html')
    if request.method == 'POST':
        inp_string = request.form.get('encode_text')
        res_str = base58.b58encode(inp_string)
        res = render_template('base58encode.html', code_string=res_str)
    return res


@app.route('/base58decode', methods=['post', 'get'])
def decoder():
    if request.method == 'GET':
        res = render_template('base58decode.html')
    if request.method == 'POST':
        inp_string = request.form.get('decode_text')
        res_str = base58.b58decode(inp_string)
        res = render_template('base58decode.html', code_string=res_str)
    return res


@app.route('/base58encode/<string:inp_string>')
def encode_string(inp_string):
    res_str = base58.b58encode(inp_string)
    res = render_template('base58encode.html', code_string=res_str)
    return res


# Case 6

@app.route('/base58decode/<string:inp_string>')
def decode_string(inp_string):
    res_str = base58.b58decode(inp_string)
    res = render_template('base58encode.html', code_string=res_str)
    return res
