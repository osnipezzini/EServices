from core import *
from core import db

from models import DBSession, Person, init_model


class Client:
    def __init__(self):
        self.session = DBSession()
        self.grid = -1
        self.type = PersonType.CLIENT

    def search(self, text, search_type='Nome'):
        q = self.session.query(Person).filter(Person.name.ilike(f"%{text}%"))
        return q.order_by(Person.name).all()

