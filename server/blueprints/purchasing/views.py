from flask import Blueprint, redirect, render_template, url_for
from ...models.models import db 
from ...models.models import (
    Vendor,
    ProductCategory,
)

from ...utils.feed import filter_by_date

purchasing = Blueprint('purchasing', __name__, template_folder="templates/purchasing", url_prefix="/purchasing")

@purchasing.route("/")
def index():
    return render_template("index.html")


@purchasing.route("/vendors")
def vendors():
    elements = {'title': 'Vendors'}
    return render_template('vendors.html', elements=elements,
                vendors=db.session.scalars(db.select(Vendor)).all())


@purchasing.route("/")
def purchase_orders():
    return render_template("purchase_orders.html")

