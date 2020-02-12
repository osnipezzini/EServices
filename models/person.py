from models import DeclarativeBase

from sqlalchemy import (BigInteger, String, Column, Sequence, Integer)


class Person(DeclarativeBase):
    __tablename__ = 'person'

    code = Column(Integer, Sequence('client_cod_seq'))
    doc = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
