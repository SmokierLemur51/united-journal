from typing import List
from flask_sqlalchemy import SQLAlchemy

from ...models.models import Customer, Contact


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
