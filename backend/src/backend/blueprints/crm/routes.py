from quart import Blueprint, current_app, render_template, redirect, url_for

from . import queries

from ...models.models import db
from ...models.models import Customer, Contact


# we are assuming crm stands for customer relationship management
crm = Blueprint(
    'crm', __name__, template_folder='templates/crm', url_prefix='/crm')


""" Test Routes """
from ...models.tests.populate import populate_customers, populate_contacts

@crm.route("/insert")
async def insert():
    with current_app.app_context():
        populate_customers(db)
        populate_contacts(db)
    return redirect(url_for('crm.customers'))


@crm.route("/list-contacts")
async def list_contacts():
    customers = queries.customers(db)
    contacts = queries.contacts(db)
    for customer in customers:
        print("\n\n{}".format(customer.company))
        for contact in contacts:
            if contact.company_id == customer.id:
                print("{} - {}".format(contact.name, contact.phone))
    return redirect(url_for('crm.home'))


""" CRM Routes """
@crm.route("/")
async def home():
    
    elements = {
        'title': 'United-Journal',
        'top_customers': None,
    }
    return await render_template('home.html', elements=elements)


@crm.route("/customers")
async def customers():
    elements = {
        'title': 'Customers',
    }
    return await render_template('customers.html', elements=elements, customers=queries.customers(db))


@crm.route("/customers/create-customer")
async def create_customer():
    pass


@crm.route("/feed")
async def feed():
    return await render_template('feed.html')


@crm.route('/customer-inquiry')
async def customer_inquiry():
    return await render_template('customer_inquiry.html')


@crm.route('/new_customer')
async def new_customer():
    return await render_template('new_customer.html')