from os import getenv

from flask import render_template
from flask_login import LoginManager, UserMixin

from . import app


class User(UserMixin):
    def __init__(self, word, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = word


# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
codewords = getenv("CODEWORDS", "").split(":")


# Authentification
@login_manager.user_loader
def user_loader(word):
    if word in codewords:
        return User(word)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template("unauthorized.html")
