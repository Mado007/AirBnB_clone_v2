#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
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


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
