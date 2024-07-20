"""
models/feed.py

Funtions to populate the feed.html page 
"""
from typing import List
from flask_sqlalchemy import SQLAlchemy

from ..models.models import Customer


""" Creating this in mind that the main feed will have many different 
    types of objects to display. 
    (Orders, Customer events, Announcements, Tasks, Notes, Requests)

    The goal is to return a list that is ordered newest to oldest varying objects. 
"""
def filter_by_date(db: SQLAlchemy, dataset: list) -> list:
    """ Params:
        -db      -> SQLAlchemy database object
        -dataset -> a list of dictionaries for each object 
            {"object": object, "where": query info for where statement or false}
    """
    filtered_list = []
    for data in dataset:
        if data["where"]:
            filtered_list.append(db.session.scalars(db.select(data["object"]).where(data["where"])).all())
        else:
            filtered_list.append(db.session.scalars(db.select(data["object"])).all())
    # filtered list is now list[list[objects]]
    return filtered_list


def populate_dataset():
    pass


def top_customers_feed(db: SQLAlchemy) -> List[Customer]:
    customers = db.session.scalars(db.select(Customer)).all()
    # customers.sort(key=lambda Customer, Customer.ytd_spent)
    return []