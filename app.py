from flask import Flask
from faker import Faker
import csv
import requests
import base58

app = Flask(__name__)
fake = Faker()

@app.route("/")
def hello_world():
    return'<p><h1>Homework 9</h1></p>'

#========================================
#===============Task1====================
#========================================

file_name = 'requirements.txt'

@app.route("/requirements/")
def read_file():
    with open(file_name, 'r') as f:
        task_1 = f.read()
        return task_1

#========================================
#===============Task2====================
#========================================

@app.route("/generate-users/<int:number>")
def create_user(number):
    users = {}
    for i in range(number):
        name=fake.name()
        email=fake.email()
        fields={name: email}
        users.update(fields)
    return users

#========================================
#===============Task3====================
#========================================

@app.route('/mean/')
def process_csv():
    try:
        with open("hw05.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            row_counter = 0
            total_height = 0
            total_weight = 0
            for row in reader:
                if row:
                    row_counter = row_counter + 1
                    total_height = total_height + float(row[1])
                    total_weight = total_weight + float(row[-1])
            high = total_height / row_counter * 2.54
            weight = total_weight / row_counter / 2.2046
            results = f"Parsed file: 'hw05.csv' <br>Total values in file (strings of data): {row_counter} \
                      <br>Average height: {high}cm <br> Average weight: {weight}kg "
            return results
    except IOError:
        return "File 'hw05.csv' not found"

#========================================
#===============Task4====================
#========================================

@app.route('/space/')
def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()

#========================================
#===============Task5====================
#========================================

@app.route('/base58encode/<string>')
def encode(string):
    return base58.b58encode(string)

#========================================
#===============Task6====================
#========================================

@app.route('/base58decode/<STRING_IN_BASE58>')
def decode(STRING_IN_BASE58):
    return base58.b58decode(STRING_IN_BASE58)