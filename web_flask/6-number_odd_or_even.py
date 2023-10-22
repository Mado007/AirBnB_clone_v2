#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """index page for my application

    Returns:
        string: to be viewed on browser
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb page for my application

    Returns:
        string: to be viewed on browser
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    """/c/<text> page for my application

    Returns:
        string: to be viewed on browser
    """
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_variable(text):
    """/python/<text> page for my application

    Returns:
        string: to be viewed on browser
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_variable(n):
    """/number/<n> page for my application

    Returns:
        string: to be viewed on browser
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_variable_template(n):
    """number_variable_template page for my application

    Returns:
        template: to be viewed on browser
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even_template(n):
    """number_odd_even_template page for my application

    Returns:
        template: to be viewed on browser
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
