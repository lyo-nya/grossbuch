from flask import render_template
from flask_login import login_required
from flask_weasyprint import HTML, render_pdf

from .. import app
from .get_data import get_data


@app.route("/invoice/<id>")
@login_required
def invoice(id):
    order = get_data("order", id, to_json=False)
    items = get_data("invoice_table", id, to_json=False)
    html = render_template('invoice.html', order=order, items=items)
    return render_pdf(HTML(string=html))
