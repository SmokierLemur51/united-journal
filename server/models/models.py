import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



class Vendor(Base):
    __tablename__ = "vendors"

    id: Mapped[int] = mapped_column(primary_key=True)
    vendor: Mapped[str] = mapped_column(String(120), unique=True)
    street: Mapped[str] = mapped_column(String(200), unique=True)
    street_2: Mapped[str] = mapped_column(String(200), nullable=True)
    city: Mapped[str] = mapped_column(String(60))
    state: Mapped[str] = mapped_column(String(25))
    zip: Mapped[str] = mapped_column(String(10))
    # relationships
    products: Mapped[list['Product']] = relationship(back_populates='vendor')

    def __repr__(self) -> str:
        return "{}".format(self.vendor)





class ProductCategory(Base):
    __tablename__ = "product_categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(120), unique=True)
    info: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # relationships
    products: Mapped[list["Product"]] = relationship(back_populates='category')
    sub_categories: Mapped[list["ProductSubCategory"]] = relationship(back_populates="parent_category")
    

    def __repr__(self) -> str:
        return "{}".format(self.category)




class ProductSubCategory(Base):
    __tablename__ = "product_sub_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_category_id: Mapped[int] = mapped_column(ForeignKey("product_categories.id"))
    sub_category: Mapped[str] = mapped_column(String(120), unique=True)
    info: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # relationships
    parent_category: Mapped["ProductCategory"] = relationship(back_populates="sub_categories")


    def __repr__(self) -> str:
        return "Sub Category: <{}>, Parent Category: <{}>".format(
            self.sub_category, self.parent_category.category)




class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    product: Mapped[str] = mapped_column(String(80))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())    
    deleted_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('product_categories.id'))
    sub_category_id: Mapped[int] = mapped_column(ForeignKey('product_sub_categories.id'))    
    vendor_id: Mapped[int] = mapped_column(ForeignKey('vendors.id'))
    product: Mapped[str] = mapped_column(String(120), unique=True)
    cost: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    selling: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    # need to add sizing dimensions

    # relationships
    category: Mapped['ProductCategory'] = relationship(back_populates='products')
    vendor: Mapped['Vendor'] = relationship(back_populates="products")
    


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())    
    deleted_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    
