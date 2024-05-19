from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from .models import Vendor, ProductCategory, Product

def populate_vendors(db: SQLAlchemy) -> None:
    # originally the vendors were outside of the func, but it makes it
    # so much easier to not have to import the list and then also pass it as a param 
    vendor_list = [
        Vendor(vendor="Dan's PVC Products", street="1293 Bardstown Rd, Louisville",
            city='Louisville', state='KY', zip="40204"),
        Vendor(vendor="Darrin Lee's Tools", street="6118 Jackson Fields Dr",
            city="Charlestown", state="IN", zip='47111'),
        Vendor(vendor="Amy's Advanced Aluminum", street='1001 Logan St', 
            city="Louisville", state='KY', zip='40204'),
        Vendor(vendor="Lauren's Vinyl Products", street="1706 Bardstown Rd",
            city="Louisville", state="KY", zip='40205'),
        Vendor(vendor="Lacey's Windows", street="745 Cochran Hill Rd",
            city="Louisville", state='KY', zip='40206'),
        Vendor(vendor="Callie's Fiber Cement", street="4901 Outer Loop",
            city='Louisville', state='KY', zip='40219'),
        Vendor(vendor="Lucas's Gutter Materials", street='4840 Outer Loop',
            city='Louisville', state='KY', zip='40219'),
        Vendor(vendor="Blair's Bold Windows", street='7311 Jefferson Blvd',
            city='Louisville', state='KY', zip='40219'),
    ]
    # add list to session and commit to database
    with current_app.app_context():
        db.session.add_all(vendor_list)
        db.session.commit()



def populate_categories(db: SQLAlchemy) -> None:
    # me being lazy again
    parent = "Parent category for"
    product_category_list = [
        ProductCategory(category='Trim Coil', info='General fascia metals, will have sub categories for pvc, preformed, etc.'),
        ProductCategory(category='Gutter Materials', 
            info="General gutter materials, sub categories for 5\"/6\" coil, and accessories."),
        ProductCategory(category='Vinyl Siding', 
            info="Vinyl siding parent category, has several sub categories for types & accessories."),
        ProductCategory(category="Fiber Cement Siding", 
            info="Parent category for fiber cement building materials. Trim, siding, etc included in sub categories."),
        ProductCategory(category="Composite Siding", 
            info="{} composite siding, sub categories for accessory and types of material.".format(parent)),
        ProductCategory(category="Decking", 
            info="{} for decking. Sub categories for accessories, clips, planks etc.".format(parent)),
        ProductCategory(category="Metal Siding", 
            info="{} for metal siding and accessories.".format(parent)),    
    ]
    # add to session and commit changes
    with current_app.app_context():
        db.session.add_all(product_category_list)
        db.session.commit()


def populate_sub_categories(db: SQLAlchemy):
    categories = db.session.scalars(db.select(ProductCategories)).all()
    sub_categories = [
        
    ]
