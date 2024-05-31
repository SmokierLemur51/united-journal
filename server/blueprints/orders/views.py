from flask import Blueprint, redirect, render_template, url_for
from ...models.models import db 
from ...models.models import (
    Vendor,
    ProductCategory,
)

orders = Blueprint('orders', __name__, template_folder="templates/orders", url_prefix="/orders")


# from ...models.populate import populate_sub_categories 
@orders.route("/")
def index():
    elements = {}
    return render_template("index.html", elements=elements)


@orders.route("/create")
def create():
    elements = {}
    return render_template("create.html", elements=elements)

