from flask import Flask

# Basic app setup
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

from . import  views
