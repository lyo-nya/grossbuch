from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base, engine


class PriceTag(Base):
    __tablename__ = "pricetags"
    id = Column(Integer, primary_key=True)
    job_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    order = relationship("OrderItem", back_populates="item")

    def as_dict(self):
        return (self.job_type, {
            self.title: {
                "unit": self.unit,
                "price": self.price,
                "id": self.id
            }
        })


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    client = Column(String)
    description = Column(String)
    order = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey("orders.id"), nullable=False)
    job_id = Column(ForeignKey("pricetags.id"))
    price = Column(Integer)
    quantity = Column(Integer)
    order = relationship("Order", back_populates="order")
    item = relationship("PriceTag", back_populates="order")

Base.metadata.create_all(bind=engine, checkfirst=True)
