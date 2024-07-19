from flask import Blueprint, current_app, render_template, redirect, url_for

from . import queries

from ...models.models import db
from ...models.models import Customer, Contact


# we are assuming crm stands for customer relationship management
crm = Blueprint(
    'crm', __name__, template_folder='templates/crm', url_prefix='/crm')


""" Test Routes """
from ...models.tests.populate import populate_customers, populate_contacts

@crm.route("/insert")
def insert():
    with current_app.app_context():
        #populate_customers(db)
        #populate_contacts(db)
        from . import populate
        populate.populate_notes(db)
    return redirect(url_for('crm.customers'))


@crm.route("/list-contacts")
def list_contacts():
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
def home():
    
    elements = {
        'title': 'United-Journal',
        'top_customers': None,
    }
    return render_template('home.html', elements=elements)


@crm.route("/customers")
def customers():
    elements = {
        'title': 'Customers',
    }
    customers = queries.customers(db)
    print(customers)
    return render_template('customers.html', elements=elements, customers=customers)


@crm.route("/customers/create-customer")
def create_customer():
    pass


@crm.route("/feed")
def feed():
    return render_template('feed.html')


@crm.route('/customer-inquiry')
def customer_inquiry():
    return render_template('customer_inquiry.html')


@crm.route('/new_customer')
def new_customer():
    return render_template('new_customer.html')


@crm.route('/customers/<int:id>')
def customer(id):
    customer = db.get_or_404(Customer, id)
    return customer.company


@crm.route('/customers/<int:id>/notes/create', methods=['GET', 'POST'])
def create_customer_note(id):
    customer = db.get_or_404(Customer, id)
    # form = CreateCustomerNoteForm()
    return "creating customer note"


@crm.route('/customers/<int:customer_id>/notes')
def customer_notes(customer_id):
    customer = db.get_or_404(Customer, customer_id)
    notes = queries.customer_notes(db, customer)
    if len(notes) == 0:
        return "No notes"
    return "Customer: {} has {} notes".format(customer.company, len(notes))


    
@crm.route('/customers/<int:customer_id>/notes/<int:note_id>/view')
def customer_note(customer_id, note_id):
    customer = db.get_or_404(Customer, customer_id)
    note = queries.customer_note(db, customer, note_id)
    return note.title
