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


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.run(host='0.0.0.0', port=5000)
