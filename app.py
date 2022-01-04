from flask import Flask, render_template
from flask import request


app = Flask(__name__)


@app.route('/hello/')
def hello():
    return '<html><body><menu><a href="/hello/">Hello</a> <a href="/about/">About</a> <a href="/contact/">Contact</a></menu><h1>Hello!</h1></body></html>'


@app.route('/about/')
def about():
    return '<html><body><menu><a href="/hello/">Hello</a> <a href="/about/">About</a> <a href="/contact/">Contact</a></menu><h1>About as...</h1></body></html>'


@app.route('/contact/')
def contact():
    return '<html><body><menu><a href="/hello/">Hello</a> <a href="/about/">About</a> <a href="/contact/">Contact</a></menu><h1>Contact me...</h1></body></html>'


# Work with URL-parameters (calculator)
@app.route('/sum/')
def index():
    return f"Sum a + b = {int(request.values.get('a')) + int(request.values.get('b'))}"


app.run(debug=True)
