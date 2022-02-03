from datetime import date

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from .. import app
from ..models import Order, OrderItem, PriceTag
from ..queries import add_item
from .get_data import get_data


# Pricetag
@app.route("/pricetag/<id>", methods=["GET", "POST"])
@login_required
def pricetag(id):
    if id == "new":
        pricetag = None
    else:
        pricetag = get_data("pricetag", id=id, to_json=False)
    if request.method == "POST":
        if not pricetag:
            pricetag = PriceTag(**request.form)
        else:
            pricetag.set_values(request.form)
        add_item(pricetag)
        return redirect(url_for("pricetag", id=id))
    hints = get_data("form_hints", to_json=False)
    return render_template("pricetags/edit.html",
                           pricetag=pricetag,
                           hints=hints)


# Order
@app.route("/order/<id>", methods=["GET", "POST"])
@login_required
def order(id):
    if id == "new":
        order = None
    else:
        order = get_data("order", id, to_json=False)
    if request.method == "POST":
        if not order:
            order = Order(date=date.today(), **request.form)
        else:
            order.set_values(request.form)
        if ("title" in request.form) and ("quantity" in request.form):
            item = OrderItem(order_id=id,
                             job_id=request.form["title"],
                             price=request.form["price"],
                             quantity=request.form["quantity"])
            add_item(item)
        add_item(order)
        id = order.id
        return redirect(url_for("order", id=id))
    if not order:
        return render_template("orders/new.html")
    items = get_data("invoice_table", id, to_json=False)
    return render_template(
        "orders/edit.html",
        order=order,
        items=items,
    )
