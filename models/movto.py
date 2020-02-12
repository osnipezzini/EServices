from sqlalchemy import Column, Date

from models import DeclarativeBase, ForeignKey, Person, relationship, Integer, String


class Movto(DeclarativeBase):
    __tablename__ = 'movto'

    data = Column(Date())
    account_debit = Column()
    person_id = Column(Integer, ForeignKey('person.grid'))
    person = relationship(Person)
    doc = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
