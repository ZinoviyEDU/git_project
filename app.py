from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)
os.environ.get('.env')


@app.route('/achievements')
def achievements():
    split_data = []
    with open('const/index.csv', mode='r') as f:
        table_data = f.readlines()
        for line in table_data:
            split_line = line.split(';')
            split_data.append(split_line)
    res = render_template('achievements.html', data=split_data)
    return res


@app.route('/')
@app.route('/SSR_GG')
def about():
    res = render_template('SSR_GG.html')
    return res


@app.route('/contact')
def contact():
    res = render_template('contact.html')
    return res


@app.errorhandler(HTTPException)
def page_not_found(e):
    if e.code == 404:
        res = render_template('404.html'), e.code
        return res
    elif e.code == 500:
        res = render_template('500.html'), e.code
        return res
