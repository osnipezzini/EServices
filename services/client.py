from sqlalchemy import update

from core import *
from core import db

from models import DBSession, Person


class Client:
    def __init__(self):
        self.session = DBSession()
        self.grid = -1
        self.type = PersonType.CLIENT

    def search(self, text, search_type='Nome'):
        if search_type == 'Nome':
            q = self.session.query(Person).filter(Person.name.ilike(f"%{text}%"))
        elif search_type == 'CPF/CNPJ':
            q = self.session.query(Person).filter(Person.doc.ilike(f"%{text}%"))
        return q.order_by(Person.name).all()

    def delete(self, grid):
        query = update(Person).where(Person.grid == grid).values(flag='D')
        return query
