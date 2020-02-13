from sqlalchemy import (String, Column, Sequence, Integer, CHAR)

from models import DeclarativeBase, DBSession

seq = Sequence('client_cod_seq')


class Person(DeclarativeBase):
    __tablename__ = 'person'

    code = Column(Integer, seq)
    doc = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    flag = Column(CHAR(1), nullable=False, default='A')
    city_code = Column(String(10), nullable=False)
    city_name = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    zipcode = Column(String(10), nullable=True)
    district = Column(String(50), nullable=True)
    country = Column(String(50), nullable=True)
    address = Column(String(50), nullable=True)
    address_nr = Column(String(50), nullable=False, default='S/N')

    def get_seq(self):
        s = DBSession()
        val = s.execute(seq)
        return val
