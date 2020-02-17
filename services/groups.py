from models import PersonGroup
from services import BaseService


class PersonGroupService(BaseService):
    def __init__(self):
        super(PersonGroupService, self).__init__(PersonGroup)

    def search(self, text, search_type='Nome', search_options=['A']):
        return super().search(text, search_options).order_by(self.model.code).limit(100).all()
