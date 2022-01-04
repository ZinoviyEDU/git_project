from flask import Flask
from markupsafe import escape
from flask import request

# print(f"__name__ = {__name__}")
app = Flask(__name__)


# localhost: 5000
@app.route("/")
def hello_world():
    return "<p><h1>Main page!</h1></p>"


@app.route('/user/<int:username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(type(request))
    print(dir(request))
    if request.method == 'POST':
        return "Do the login"
    else:
        return "Show the login form"