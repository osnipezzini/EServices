from sqlalchemy import update

from core import *
from core import db

from models import DBSession, Person


class Client:
    def __init__(self):
        self.grid = -1
        self.type = PersonType.CLIENT
        self.model = None

    def search(self, text, search_type='Nome'):
        session = DBSession()
        if search_type == 'Nome':
            q = session.query(Person).filter(Person.name.ilike(f"%{text}%"))
        elif search_type == 'CPF/CNPJ':
            q = session.query(Person).filter(Person.doc.ilike(f"%{text}%"))
        return q.filter(Person.flag == 'A').order_by(Person.name).all()

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
