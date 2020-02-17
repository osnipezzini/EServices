from sqlalchemy import func

from core import log
from models import DBSession


class BaseService:
    def __init__(self, model):
        self.grid = -1
        self.model = model

    def search(self, text, search_options=['A']):
        session = DBSession()
        q = session.query(self.model).filter(self.model.name.ilike(f"%{text}%"))
        return q.filter(self.model.flag.in_(search_options))

    def delete(self, grid):
        session = DBSession()
        session.query(self.model).filter(self.model.grid == grid).update({'flag': 'D'})
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
        session.query(self.model).filter(self.model.grid == grid).update(data)
        try:
            session.commit()
        except Exception as e:
            log.debug("Ocorreu um erro ao salvar as configurações !\n" + e)
            session.rollback()

    def get_next_code(self):
        session = DBSession()
        q = session.query(func.max(self.model.code))
        return q.first()[0]

    def get(self, grid):
        session = DBSession()
        q = session.query(self.model).get(int(grid))
        return q