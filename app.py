import csv
import json
import os
import base58
import requests
from flask import Flask
from faker import Faker

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<pre>Welcome to Homework_9!\n\n" \
           "Please select one of the options by entering" \
           " the name of the option in the link of this server:\n\n" \
           "/requirements - review requirements.txt\n" \
           "/generate-users/xx, xx - the number of users you want to view\n" \
           "/mean - .csv file analysis\n" \
           "/space - view information about astronauts\n" \
           "/base58encode/string, string - string to encode in base58\n" \
           "/base58decode/string_in_base58, " \
           "string_in_base58 - the encoded string in base58 is decoded " \
           "into the original string</pre>"


@app.route("/requirements")
def show_requirements():
    with open('requirements.txt', 'r') as f:
        return f'<pre>{f.read()}</pre>'


@app.route("/generate-users/<int:xx>")
def generate_users(xx: int):
    fake = Faker()
    names_list = []
    for i in range(xx):
        i = fake.name() + ', ' + fake.email()
        names_list.append(i)
    names_str = '\n'.join(names_list)
    return f'<pre>{names_str}</pre>'


@app.route("/mean")
def mean():
    with open('hw9.csv', 'r') as f:
        strings_count = 0
        reader = csv.DictReader(f)
        heights = []
        weights = []
        for row in reader:
            strings_count += 1
            values = dict(row)
            heights.append(values.get(' "Height(Inches)"'))
            weights.append(values.get(' "Weight(Pounds)"'))
        float_heights = [float(item) for item in heights]
        float_weights = [float(item) for item in weights]
        average_height = sum(float_heights) / len(float_heights)
        average_weight = sum(float_weights) / len(float_weights)

    return f'<pre>Parsed file: {os.path.basename("hw9.csv")}\n' \
           f'Total values in file (strings of data): {strings_count}\n' \
           f'Average height: {average_height} cm\n' \
           f'Average weight: {average_weight} kg</pre>'


@app.route("/space")
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    r_json = r.json()
    return f'<pre>{json.dumps(r_json, indent=4, sort_keys=True)}</pre>'


@app.route("/base58encode/<string>")
def base58encode(string):
    string_in_base58 = base58.b58encode(string).decode('utf-8')
    return f'<pre>Encoding {string} to base58: {string_in_base58}</pre>'


@app.route("/base58decode/<string_in_base58>")
def base58decode(string_in_base58):
    string_from_base58 = base58.b58decode(string_in_base58).decode('utf-8')
    return f'<pre>Decoding {string_in_base58} ' \
           f'from base58: {string_from_base58}</pre>'
