from flask import Blueprint, current_app, render_template, redirect, url_for

from ..models.models import db
from ..models.models import Customer


# we are assuming crm stands for customer relationship management
crm = Blueprint(
    'crm', __name__, template_folder='templates/crm', url_prefix='/crm')


""" Test Routes """
from ..models.tests.populate import populate_customers

@crm.route("/insert")
def insert():
    with current_app.app_context():
        populate_customers(db)
    return redirect(url_for('crm.customers'))


""" CRM Routes """
@crm.route("/")
def home():
    elements = {
        'title': 'United-Journal',
    }
    return render_template('home.html', elements=elements)


@crm.route("/customers")
def customers():
    elements = {
        'title': 'Customers',
        'customers': db.session.scalars(db.select(Customer)).all(), # default customers sorted by ytd-spent  
    }
    for c in elements['customers']:
        print(c.company)

    return render_template('customers.html', elements=elements)


@crm.route("/feed")
def feed():
    return render_template('feed.html')
