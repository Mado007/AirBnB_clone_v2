#!/usr/bin/python3
"""nodule documentation for 0-routing in"""


from web_flask import app


@app.route("/", strict_slashes=False)
def index():
    """index page for my application

    Returns:
        _type_: string to be viewed on browser
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.run(host='0.0.0.0', port=5000)
