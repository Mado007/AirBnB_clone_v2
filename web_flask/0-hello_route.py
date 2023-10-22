from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = True

@app.route("/")
def index():
    return 'Hello HBNB!'
