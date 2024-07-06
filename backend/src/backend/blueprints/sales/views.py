from flask import Blueprint, redirect, render_template, url_for
from ...models.models import db 
from ...models.models import (
    Vendor,
    ProductCategory,
)

from ...utils.feed import filter_by_date

sales = Blueprint('sales', __name__, template_folder="templates/sales", url_prefix="/")


# from ...models.populate import populate_sub_categories 
@sales.route("/testing/populate-tables")
def populate_with_test_data():
    # populate_sub_categories(db)
    return redirect(url_for('sales.vendors'))


@sales.route("/")
def home():
    # General overview of current feed
    elements={
        'title': 'Sales',
        # 'feed': filter_by_date(db, 
        #     [
        #         {"object": Vendor, "where": False},
        #         {"object": ProductCategory, "where": False},
        #     ]    
        # ),
    }
    return render_template('home.html', elements=elements)

