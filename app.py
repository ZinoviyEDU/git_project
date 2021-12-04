from flask import Flask

app = Flask(__name__)

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