from typing import List
from flask_sqlalchemy import SQLAlchemy

from ...models.models import (
    Customer, CustomerNote, Contact,
)

def customer(db: SQLAlchemy, id: int):
    return db.session.scalar(db.select(Customer).where(Customer.id == id)).first()


def customers(db: SQLAlchemy) -> List[Customer]:
    return db.session.scalars(db.select(Customer)).all()


def contacts(db: SQLAlchemy) -> List[Contact]:
    return db.session.scalars(db.select(Contact)).all()


def feed():
    return 

def top_customers(db: SQLAlchemy, size: int) -> List[Customer]:
    all_customers = customers(db)
    if size == None:
        return all_customers
    return all_customers.sort(key=lambda customer: customer.ytd_spent)


def customer_notes(db: SQLAlchemy, c: Customer) -> List[CustomerNote]:
    return db.session.scalars(
        db.select(CustomerNote).where(CustomerNote.customer_id == c.id)).all()


def customer_note(db: SQLAlchemy, c: Customer, n: int) -> CustomerNote:
    return db.session.scalar(
        db.select(CustomerNote)
            .where(CustomerNote.customer_id == c.id)
            .where(CustomerNote.id == n)
    ).first()
