from flask import redirect, render_template, request, url_for
from flask_login import login_user

from .. import app
from ..auth import User


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    user = User(request.form["word"])
    login_user(user)
    return redirect(url_for("pricelist"))
