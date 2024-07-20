from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import IntegrityError

from ..models import (
    Vendor, ProductCategory, ProductSubCategory, Product,
    Customer, Contact,
)
from ..queries import query_category_id_by_name
from .util import random_customer


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
        try:
            db.session.add_all(vendor_list)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        except Exception as e:
            print(e)
            db.session.rollback()


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
        try:
            db.session.add_all(product_category_list)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        except Exception as e:
            print(e)
            db.session.rollback()


def populate_sub_categories(db: SQLAlchemy) -> None:
    sub_categories = [
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="6\" Coil",
            info="6\" Gutter Coil",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="3x4 Downspouts",
            info="3x4 downspouts for 6\" gutters",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="3x4 A Style Elbows",
            info="3x4 a elbows for 6\" gutters",        
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="3x4 B Style Elbows",
            info="3x4 b elbows for 6\" gutters",        
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="3x4 A Style Ledge Jumping Elbows",
            info="3x4 a style ledge jumpers for 6\" gutters",        
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="5\" Coil",
            info="5\" Gutter Coil",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="2x3 Downspouts",
            info="2x3 downspouts for 5\" gutters",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="2x3 A Style Elbows",
            info="2x3 a elbows for 5\" gutters",        
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="2x3 B Style Elbows",
            info="2x3 b elbows for 5\" gutters",        
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Gutter Materials"),
            sub_category="2x3 A Style Ledge Jumping Elbows",
            info="2x3 a style ledge jumpers for 5\" gutters",        
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Trim Coil"),
            sub_category=".024 PVC Coil",
            info=".024 PCV Coil, pvc striated rolled fascia metal.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Trim Coil"),
            sub_category=".018 Aluminum Coil",
            info=".018 Aluminum Coil, builder-grade aluminum rolled fascia metal.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Trim Coil"),
            sub_category=".024Aluminum Coil",
            info=".024 Aluminum Coil, high-grade aluminum rolled fascia metal.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Vinyl Siding"),
            sub_category="Vinyl Siding",
            info="Vinyl siding options",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Vinyl Siding"),
            sub_category="Corner Posts",
            info="Vinyl corner posts",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Vinyl Siding"),
            sub_category="J-Channel",
            info="Vinyl j-channel options",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Vinyl Siding"),
            sub_category="Finish Trim",
            info="Vinyl finish trim",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Vinyl Siding"),
            sub_category="Starter Strips",
            info="Starter strip options, not necessarily made of vinyl, but designed for it.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 8-1/4 Cedar Mill",
            info="James hardie cedar mill 8-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 8-1/4 Smooth",
            info="James hardie smooth 8-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 7-1/4 Cedar Mill",
            info="James hardie cedar mill 7-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 7-1/4 Smooth",
            info="James hardie smooth 7-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 6-1/4 Cedar Mill",
            info="James hardie cedar mill 6-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 6-1/4 Smooth",
            info="James hardie smooth 6-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 5-1/4 Cedar Mill",
            info="James hardie cedar mill 5-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 5-1/4 Smooth",
            info="James hardie smooth 5-1/4 profile.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 5/4 Smooth Trim Boards",
            info="James hardie 5/4 smooth trim boards.",
        ),
        ProductSubCategory(
            parent_category_id=query_category_id_by_name(db, "Fiber Cement Siding"),
            sub_category="James Hardie 4/4 Smooth Trim Boards",
            info="James hardie 4/4 smooth trim boards.",
        ),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(sub_categories)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        except Exception as e:
            print(e)
            db.session.rollback()


def populate_gutter_coil(db: SQLAlchemy) -> None:
    colors = [
        "30 deg white","almond", "black", "cameo", "charcoal grey",
        "classic cream", "dark bronze", "desert sand", "everest",
        "evergreen", "harbor grey", "linen", "montana suede", 
        "musket brown", "pebblestone clay", "royal brown", "rugged canyon",
        "sandtone", "silver grey", "terra bronze", 
        "victorian grey", "wicker",
    ]
    requirements = []
    for c in colors:

        with current_app.app_context():
            try:
                db.session.add(coil)
                db.session.commit()
            except Exception as e:
                print("\nError: \n{}\n{}\n\n".format(e, coil.color))
                db.session.rollback()


def populate_customers(db: SQLAlchemy) -> None:
    customers = [
        Customer(
            company="All-Star Construction LLC",
            street="123 Star Ave",
            city="Louisville",
            state="KY",
            zip="40219",
        ),
        Customer(
            company="Append Additions LLC",
            street="432 Murray Ave",
            city="Louisville",
            state="Ky",
            zip="40219",
        ),
        Customer(
            company="Higginbotham Painting LLC",
            street="123 Capitial St",
            city="Corydon",
            state="IN",
            zip="47111",
        ),
        Customer(
            company="Excellent Remodeling LLC",
            street="90 Houston Blvd",
            city="Louisville",
            state="KY",
            zip="40204",
        ),
        Customer(
            company="Party Rock Gutters LLC",
            street="78 Custom Blvd",
            city="Louisville",
            state="KY",
            zip="40204",
        ),
        Customer(
            company="Evolve Remodeling",
            street="54 Calle Sol Ave",
            city="Louisville",
            state="KY",
            zip="50303",
        ),
        Customer(
            company="Bob The Builder",
            street="92 Montana Ave",
            city="Louisville",
            state="KY",
            zip="40424",
        ),
        Customer(
            company="Star Construction", 
            street="120 W Main St",
            city="Louisville",
            state="KY", zip="40123",
        ),
        Customer(
            company="Extreme Restorations", 
            street="100 N Second St",
            city="Louisville",
            state="KY", zip="40214",
        ),
        Customer(
            company="Impressive Improvements Inc", 
            street="2 Logan St",
            city="Louisville",
            state="KY", zip="40214",
        ),
        Customer(
            company="Professional Handyman Services", 
            street="98 Bell Ave",
            city="Louisville", state="KY", zip="40122",
        ),
        Customer(
            company="Average Joe's Roofers", 
            street="16 Defeat St",
            city="Louisville", state="KY", zip="40152",
        ),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(customers)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)


def populate_contacts(db: SQLAlchemy) -> None:
    customers = db.session.scalars(db.select(Customer)).all()
    contacts = [
        Contact(
            company_id=random_customer(customers).id,
            name="Mark",
            phone="1921942342",
            email="mark@mark.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Steve",
            phone="1031238945",
            email="steve@gmail.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Darrin",
            phone="7891236745",
            email="darrin@gmail.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Sam",
            phone="0987654564",
            email="sam@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Carl",
            phone="8764538979",
            email="carl@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Javier",
            phone="8760348765",
            email="javier@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Heine",
            phone="4563452637",
            email="heine@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Marinara",
            phone="1029384756",
            email="marinara@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Scandra",
            phone="8749998888",
            email="scandra@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Cal",
            phone="6751238576",
            email="cal@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Estrella",
            phone="6567677666",
            email="estrella@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Colton",
            phone="1237894567",
            email="colton@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Merl",
            phone="7825673456",
            email="merl@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Bart",
            phone="34232143333",
            email="bart@gmail.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Bertha",
            phone="0001119999",
            email="bertha@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Martha",
            phone="8883337777",
            email="martha@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Samuela",
            phone="8889990000",
            email="samuela@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Tabatha",
            phone="7776664848",
            email="tabatha@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Elroy",
            phone="4443332222",
            email="elroy@test.com",
        ),
        Contact(
            company_id=random_customer(customers).id,
            name="Fairis",
            phone="0007891234",
            email="fairis@test.com",
        ),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(contacts)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)



""" Nothing below """
def populate_all(db: SQLAlchemy) -> None:
    populate_vendors(db)
    populate_categories(db)
    populate_sub_categories(db)
    # populate_gutter_coil(db)
    populate_customers(db)
    populate_contacts(db)