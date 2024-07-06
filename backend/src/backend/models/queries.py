"""
File: models/queries.py

This file is for common queries. Hopefully to save some time.
"""
from flask_sqlalchemy import SQLAlchemy

from .models import ProductCategory

def query_category_id_by_name(db: SQLAlchemy, category: str) -> int:
    c = db.session.scalars(db.select(ProductCategory).where(ProductCategory.category == category)).first()
    if c:
        return c.id
    else:
        return 0

