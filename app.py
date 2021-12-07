from flask import Flask
from faker import Faker
import pandas as pd
import requests
import base58

app = Flask(__name__)


@app.route("/requirements")
def requirements():
    with open("requirements.txt", "r") as f:
        r = f.read()
    return f"<pre>{r}</pre>"


@app.route("/generate-users/<XX>")
def person_generator(XX):
    fake = Faker()
    fake_data_list = ''

    for i in range(int(XX)):
        fake_full_name = fake.name()
        fake_name = fake_full_name.split()[0]
        fake_email_name = ''.join(fake_full_name.lower().split())
        fake_provider = fake.domain_name()
        fake_data = f"<p> {fake_name} {fake_email_name}@{fake_provider}</p>"
        fake_data_list += ''.join(fake_data)

    return f"<p>{fake_data_list}</p>"


@app.route("/mean")
def mean_calculator():
    file = 'hw05.csv'
    with open(file,"r") as f:
        data = pd.read_csv(f)
        row_count = len(data.index)
        mean_height = round(data[' "Height(Inches)"'].mean())
        mean_weight = round(data[' "Weight(Pounds)"'].mean())

    return f"<p>Parsed file: {file}</p><p>Total values in file (strings of data): {row_count}</p>\
            <p>Average height: {mean_height} cm</p><p>Average weight: {mean_weight} kg</p>"


@app.route("/space")
def astros_list():
    r = requests.get('http://api.open-notify.org/astros.json').json().get('people')
    astros = ''
    for i in r:
        astros += f"<p>Name: {i.get('name')}, craft : {i.get('craft')}</p>"

    return f"<p>{astros}</p>"


@app.route("/base58encode/<string_to_encode>")
def encode_base58(string_to_encode):
    global encoded_string
    encoded_string = base58.b58encode(string_to_encode)
    return f"<p>{encoded_string}</p>"


@app.route("/base58decode/<string_to_decode>")
def decode_base58(string_to_decode):
    string_to_decode = str(string_to_decode).replace('\'','').replace('b','')
    decoded_string = base58.b58decode(string_to_decode)
    return f"<p>{decoded_string}</p>"


if __name__ == "__main__":
    app.run()
