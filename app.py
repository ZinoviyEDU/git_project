from flask import Flask, render_template
from faker import Faker
import requests
import base58
import csv

faker = Faker()
app = Flask(__name__)
app.run(debug=True)


@app.route('/requirements/')
def read_requirements():
    try:
        with open('requirements.txt') as file:
            requirements = file.read()
            output = render_template('main.html', requirements=requirements)
        return output
    except IOError:
        return "File 'requirements.txt' not found"


@app.route('/generate-users/<int:number>')
def fake_user(number):
    if number == 0:
        return "Please input a positive number"
    else:
        result = []
        for x in range(number):
            result.append('\n')
            result.append(faker.first_name())
            result.append(faker.email())
            result.append('\n')
        string = ' '.join([str(item) for item in result])
        output = render_template('main.html', fakes=string)
        return output


@app.route('/mean/')
def process_csv():
    try:
        with open("hw05.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            row_count = 0
            sum_of_highs = 0
            sum_of_weight = 0
            for row in reader:
                if row:
                    row_count = row_count + 1
                    sum_of_highs = sum_of_highs + float(row[1])
                    sum_of_weight = sum_of_weight + float(row[-1])
            high = sum_of_highs / row_count * 2.54
            weight = sum_of_weight / row_count / 2.2046
            results = f"Parsed file: 'hw05.csv' <br>Total values in file (strings of data): {row_count} \
                      <br>Average height: {high}cm <br> Average weight: {weight}kg "
            return results
    except IOError:
        return "File 'hw05.csv' not found"


@app.route('/space')
def count_astronauts():
    response = requests.get('http://api.open-notify.org/astros.json').json()
    # return f"{len(response['people'])} people are in space now!"
    return f"{response['number']} people are in space now!"


@app.route('/base58encode/<string>')
def encode(string):
    return base58.b58encode(string)


@app.route('/base58decode/<encoded_string>')
def decode(encoded_string):
    return base58.b58decode(encoded_string)
