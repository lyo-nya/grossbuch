from flask import redirect, url_for
from flask_login import login_required

from .. import app
from .get_data import get_data, delete_items


## DELETE
@app.route("/delete/<obj_type>/<id>", methods=["GET"])
@login_required
def delete(obj_type, id):
    after = "pricelist"
    if obj_type == "pricetag":
        pricetag = get_data("pricetag", id, to_json=False)
        delete_items(pricetag)
    elif obj_type == "order":
        items = get_data("orderitems", id, to_json=False)
        delete_items(*items)
        after = "orders"
    elif obj_type == "orderitem":
        item = get_data("item", id, to_json=False)
        delete_items(item)
        return redirect(url_for("order", id=item.order_id))
    return redirect(url_for(after))
