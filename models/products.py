from sqlalchemy.orm import relationship

from models import Base, Person

from sqlalchemy import (BigInteger, String, Column, Sequence, Integer, Float, ForeignKey)


class Product(Base):
    __tablename__ = 'product'

    code = Column(Integer, Sequence('product_cod'), unique=True)
    barcode = Column(String(50), nullable=False)
    name = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
    person_id = Column(Integer, ForeignKey('person.grid'))
    person = relationship(Person)
