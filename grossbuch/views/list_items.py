from flask import render_template
from flask_login import login_required

from .. import app
from .get_data import get_data


# Pricelist
@app.route("/")
@app.route("/pricelist")
@login_required
def pricelist():
    pricelist = get_data("pricelist", to_json=False)
    return render_template("pricetags/list.html", pricelist=pricelist)


# Orders
@app.route("/orders")
@login_required
def orders():
    orders = get_data("orders", to_json=False)
    return render_template("orders/list.html", orders=orders)
