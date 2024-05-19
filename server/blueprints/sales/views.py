from flask import Blueprint, redirect, render_template, url_for
from ...models.models import db 
from ...models.models import (
    Vendor,
    ProductCategory,
)

sales = Blueprint('sales', __name__, template_folder="templates/sales", url_prefix="/sales")


from ...models.populate import populate_vendors, populate_categories 
@sales.route("/testing/populate-tables")
def populate_with_test_data():
    populate_vendors(db)
    populate_categories(db)
    return redirect(url_for('sales.vendors'))




@sales.route("/")
def home():
    elements={'title': 'Sales'}
    return render_template('home.html', elements=elements)


@sales.route("/vendors")
def vendors():
    elements = {'title': 'Vendors'}
    return render_template('vendors.html', elements=elements,
                vendors=db.session.scalars(db.select(Vendor)).all())
