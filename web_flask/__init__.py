#!/usr/bin/python3
"""webflask package init file"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
