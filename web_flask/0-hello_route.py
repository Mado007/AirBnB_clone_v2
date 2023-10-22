#!/usr/bin/python3
"""nodule documentation for 0-routing in"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """index page for my application

    Returns:
        _type_: string to be viewed on browser
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.run()
