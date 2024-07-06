""" File: models/tests/warehouses.py
"""
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import IntegrityError

from ..models import Warehouse


def populate_warehouses(db: SQLAlchemy) -> None:
    warehouses = [
        Warehouse(),
        Warehouse()
    ]

    with current_app.app_context():
        try:
            db.session.add_all(warehouses)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(e)

    