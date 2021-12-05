import csv
import base58
import requests

from flask import Flask
from faker import Faker


fake = Faker()

app = Flask(__name__)
# app.run(debug=True, use_debugger=False, use_reloader=False)


# task1 return requirements.txt
@app.route('/requirements/')
def return_requirements():
    result = ''
    with open('requirements.txt', encoding='utf-8') as file:
        for line in file:
            result += f'{line}'
    return f'<pre>{result}</pre>'


@app.route('/')
def hello_world():
    return '<p><h1>hey, there<pre>hw9</pre></h1></p>'


# task2 generate fake users and emails

@app.route('/generate-users/<int:count>')
def generate_users(count):
    result = ''
    for _ in range(count):
        result += f'{fake.first_name()} {fake.email()}\n'
    return f'<pre>{result}</pre>'

# task3
# Return average height and weight


@app.route('/mean/')
def average():
    FILE_NAME_CSV = 'hw05.csv'
    CONST_INCHES_TO_CM = 2.54
    CONST_POUNDS_TO_KG = 0.453592

    with open(FILE_NAME_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        height_sum, weight_sum = 0, 0
        count = 0

        for row in reader:
            height, weight = [row.get(' "Height(Inches)"'), row.get(' "Weight(Pounds)"')]
            height_sum += float(height)
            weight_sum += float(weight)
            count += 1

    height_avr = height_sum / count
    weight_avr = weight_sum / count

    height_avr_cm = round(height_avr * CONST_INCHES_TO_CM)
    weight_avr_kg = round(weight_avr * CONST_POUNDS_TO_KG)

    result = f"Parsed file: '{FILE_NAME_CSV}'\n"
    result += f"Total values in file (strings of data): {count}\n"
    result += f"Average height: {height_avr_cm} cm\n"
    result += f"Average weight: {weight_avr_kg} kg\n"

    return f'<pre>{result}</pre>'


# task 4
#Display the number of astronauts at the moment

@app.route('/space')
def astronauts_number():
    response = requests.get('http://api.open-notify.org/astros.json').json()
    # return f"{len(response['people'])} people are in space now!"
    return f"Number of astronauts: {response['number']} "


# task 5 encode input string

@app.route('/base58encode/<string:s>/')
def encode_base58(s):
    if ' ' in s:
        return 'The string cannot contain spaces'
    else:
        return base58.b58encode(s)


# task 6 decode input string

@app.route('/base58decode/<string:s>/')
def decode_base58(s):
    if ' ' in s:
        return 'The string cannot contain spaces'
    else:
        return base58.b58decode(s)
