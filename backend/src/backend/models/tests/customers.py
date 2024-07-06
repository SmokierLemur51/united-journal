from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from ..models import db
from ..models import Customer, CustomerContact


def populate_customers(db: SQLAlchemy) -> None:
    # All fake companies, with fake addresses
    customers = [
        Customer(
            company="Star Construction", street="120 W Main St",
            street_2="", city="",
            state="", zip="",
        ),
        Customer(
            company="", street="",
            street_2="", city="",
            state="", zip="",
        ),
        Customer(
            company="", street="",
            street_2="", city="",
            state="", zip="",
        ),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(customers)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)


def populate_customer_contacts(db: SQLAlchemy) -> None:
    contacts = []
    with current_app.app_context():
        try:
            db.session.add_all(contacts)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)
