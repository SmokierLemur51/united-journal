import random
from typing import List
from flask import current_app
from flask_sqlalchemy import SQLAlchemy 

from ...models.models import Customer, CustomerNote
from . import queries

def mr_rando(c: List[Customer]) -> int:
    return c[random.randint(0, (len(c)-1))].id



def populate_notes(db: SQLAlchemy):
    customers = queries.customers(db)
    notes = [
        CustomerNote(
            customer_id=mr_rando(customers),
            title="jafldk", 
            content="dfadfadfafd",
        ),
        CustomerNote(
            customer_id=mr_rando(customers),
            title="grgar",
            content="gaagagbruj",
        ),
        CustomerNote(
            customer_id=mr_rando(customers),
            title="uytrdfgytrd",
            content="daghathr",
        ),
        CustomerNote(
            customer_id=mr_rando(customers),
            title="fghutred",
            content="xcvbhytredf",
        ),
        CustomerNote(
            customer_id=mr_rando(customers),
            title="ftyred",
            content="d56uhredfghy65r",
        ),
        CustomerNote(
            customer_id=mr_rando(customers),
            title="sadfhad",
            content="ahjaghegaewgah",
        ),
        CustomerNote(
            customer_id=mr_rando(customers),
            title="ssssdfa",
            content="fadfafdafdfad",
        ),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(notes)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)

