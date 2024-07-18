from quart import Blueprint, redirect, render_template, url_for
from ...models.models import db 
from ...models.models import (
    Vendor,
    ProductCategory,
)

orders = Blueprint('orders', __name__, template_folder="templates/orders", url_prefix="/orders")


# from ...models.populate import populate_sub_categories 
@orders.route("/")
async def index():
    elements = {}
    return await render_template("index.html", elements=elements)


@orders.route("/create")
async def create():
    elements = {}
    return await render_template("create.html", elements=elements)

