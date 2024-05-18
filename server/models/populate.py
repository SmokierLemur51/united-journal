from flask_sqlalchemy import SQLAlchemy

from .models import Vendor, ProductCategory, Product

vendor_list = [
    Vendor(vendor="Dan's PVC Products", street=""),
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

populate_vendors(db: SQLAlchemy, vendors: list[Vendor]) -> None:
    with current_app.app_context():
        db.session.add_all(vendors)
        db.session.commit()

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

def populate_categories(db: SQLAlchemy, categories: list[ProductCategory]) -> None:
    with current_app.app_context():
        db.session.add_all(categories)
        db.session.commit()


sub_category_list = [
    
]
