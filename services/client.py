from sqlalchemy import update, func
from sqlalchemy.orm.strategy_options import joinedload

from core import *
from core import db

from models import DBSession, Person, PersonGroup
from services import BaseService


class ClientService(BaseService):
    def __init__(self):
        super(ClientService, self).__init__(Person)
        self.grid = -1
        self.type = PersonType.CLIENT

    def search(self, text, search_type='Nome', search_options=['A']):
        session = DBSession()
        q = super().search(text, search_options)
        if search_type == 'CPF/CNPJ':
            q = session.query(Person).filter(Person.doc.ilike(f"%{text}%"))
        return q.order_by(Person.name).limit(100).all()

    def delete(self, grid):
        session = DBSession()
        session.query(Person).filter(Person.grid == grid).update({'flag': 'D'})
        try:
            session.commit()
            log.info("Comando executado com sucesso !")
            log.info(session)
            return session
        except Exception as e:
            log.debug("Ocorreu um erro ao salvar as configurações !\n" + e.__str__())
            session.rollback()
            return None

    def update(self, grid, data):
        session = DBSession()
        session.query(Person).filter(Person.grid == grid).update(data)
        try:
            session.commit()
        except Exception as e:
            log.debug("Ocorreu um erro ao salvar as configurações !\n" + e)
            session.rollback()

    def get_next_code(self):
        session = DBSession()
        q = session.query(func.max(Person.code))
        return q.first()[0]

    def get(self, grid):
        session = DBSession()
        q = session.query(Person).get(int(grid))
        group = session.query(PersonGroup).get(q.group_grid)
        setattr(q, 'group_name', group.name)

        return q
