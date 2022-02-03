from flask import jsonify
from flask_login import login_required

from .. import app
from ..queries import *


def get_pricelist(*args):
    data = {}
    pricetags = pricelist_query.all()
    for pricetag in pricetags:
        job_type, pricetag_dict = pricetag.as_dict()
        data[job_type] = data.get(job_type, {})
        data[job_type].update(pricetag_dict)
    return data


def get_orders_list(*args):
    data = [order._asdict() for order in orders_query.all()]
    return data


def get_form_hints(*args):
    job_types = jobtypes_query.all()
    units = units_query.all()
    data = {
        "units": [u for u, in units],
        "job_types": [jt for jt, in job_types]
    }
    return data


def get_invoice_table(table, id, *args):
    data = order_items_prices(id)
    data = [item._asdict() for item in data]
    return data


def get_items_by_id(table, id):
    if table == "pricetag":
        data = pricetag_query(id)
    elif table == "order":
        data = order_query(id)
    elif table == "item":
        data = item_query(id)
    elif table == "orderitems":
        data = order_items_query(id).all()
        order = get_data("order", id, to_json=False)
        data.append(order)
    else:
        return []
    return data


def dummy_func(*args):
    return {}


handler_dict = {
    "pricelist": get_pricelist,
    "orders": get_orders_list,
    "form_hints": get_form_hints,
    "invoice_table": get_invoice_table,
    "pricetag": get_items_by_id,
    "order": get_items_by_id,
    "item": get_items_by_id,
    "orderitems": get_items_by_id,
}


## GET DATA
@app.route("/data/<table>")
@app.route("/data/<table>/<id>")
@login_required
def get_data(table, id=None, to_json=True):
    handle = handler_dict.get(table, dummy_func)
    data = handle(table, id)
    if to_json:
        return jsonify(data)
    else:
        return data
