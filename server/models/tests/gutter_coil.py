
from flask_sqlalchemy import SQLAlchemy

from ..models import ProductCategory, ProductSubCategory, Product


def populate_guttercoil(db: SQLAlchemy) -> None:
    mastic_coils = [
        "30 deg white","almond", "black", "cameo", "charcoal grey",
        "classic cream", "dark bronze", "desert sand", "everest",
        "evergreen", "harbor grey", "linen", "montana suede", 
        "musket brown", "pebblestone clay", "royal brown", "rugged canyon",
        "sandtone", "silver grey", "terra bronze", 
        "victorian grey", "wicker",
    ]
    # params
    p = {
        "vendor": db.session.scalar(db.select(Vendor).where(Vendor.vendor == "Lucas's Gutter Materials")).first(),
        "category": db.session.scalar(db.select(ProductCategory).where(ProductCategory.category == "Gutter Materials")).first(),
        "five_inch": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "Five \"")).first(),
        "e2x3a": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "2x3 A Style Elbows")).first(),
        "e2x3b": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "2x3 B Style Elbows")).first(),
        "ds2x3": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "2x3 Downspouts")).first(),
        "e2x3a30": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "2x3 A Style Ledge Jumping Elbows")).first(),
        "six_inch": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "Six \"")).first(),
        "e3x4a": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "3x4 A Style Elbows")).first(),
        "e3x4b": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "3x4 B Style Elbows")).first(),
        "ds3x4": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "3x4 Downspouts")).first(),
        "e3x4a30": db.session.scalar(db.select(ProductSubCategory).where(ProductSubCategory.sub_category == "3x4 A Style Ledge Jumping Elbows")).first(),
    }
    for c in mastic_coils:
        insertions = [
            # Five inch coil 
            Product(
                vendor_id=p["vendor"].id, 
                category_id=p["category"].id, 
                sub_category_id=p['five_inch'].id,
                product="",
                ),
            # 
        ]
        
        
