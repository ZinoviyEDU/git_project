from flask import Flask, request, render_template
from werkzeug.exceptions import HTTPException
import csv
import json
from dotenv import load_dotenv

load_dotenv('.env')
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    split_data = []
    with open('data/index.csv', mode='r') as fh:
        table_data = fh.readlines()
        for line in table_data:
            split_line = line.split(';')
            split_data.append(split_line)
    res = render_template('index.html', data=split_data)
    return res


@app.route('/about')
def about():
    res = render_template('about.html')
    return res


@app.route('/contact_us', methods=['POST', 'GET'])
def contact_us():
    form_payload = {}
    if request.method == 'GET':
        res = render_template('contact_us.html')
    elif request.method == 'POST':
        form_payload['firstname'] = request.form.get('firstname')
        form_payload['lastname'] = request.form.get('lastname')
        form_payload['email'] = request.form.get('email')
        form_payload['message_type'] = request.form.get('message_type')
        form_payload['response'] = request.form.get('response')
        form_payload['comment'] = request.form.get('comment')
        with open('data/form_data.txt', mode='a') as fh:
            fh.write(json.dumps(form_payload)+'\n')
        res = render_template('contact_us.html')
    return res


@app.errorhandler(HTTPException)
def page_not_found(e):
    res = e.description
    if e.code == 404:
        res = render_template('404.html'), e.code
    elif e.code == 500:
        res = render_template('500.html'), e.code
    return res

