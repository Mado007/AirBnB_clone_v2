#!/usr/bin/python3
"""nodule documentation for 0-routing in flask"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
