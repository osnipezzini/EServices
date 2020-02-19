from core import get_icon
from ui.main_ui import MainUi


class MainView(MainUi):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.SetIcon(get_icon())
        self.SetSize((800, 600))
        self.Maximize()
        self.Centre()
        # from models.person import Person, PersonGroup
        #
        # session = DBSession()
        #
        # group = PersonGroup(name="CLIENTES")
        # session.add(group)
        # session.commit()
        # session.flush()
        # print(group.grid)
        # # # Insert a Person in the person table
        # new_person = Person(name='Osni Pezzini Jr', email='teste@teste.com', doc='000.000.000-00',
        #                     city_code=4202404, city_name='Blumenau', state='SC', zipcode='89037-430',
        #                     district='Água Verde', country='Brasil', address='Rua Martinha Eskelsen', address_nr='45',
        #                     group_grid=group.grid
        #                     )
        # session.add(new_person)
        # session.commit()
        # session.flush()
        # #
        # product = Product(barcode='0000021212', name='Produto teste', price=10.0, person=new_person)
        # session.add(product)
        # session.commit()
        # session.flush()
        # for user, product in session.query(Person, Product):
        #     print(product.person)

    def open_client(self, event):
        from views.create.client import ClientView
        gui = ClientView(self)

        gui.Show()

    def open_product(self, event):
        from views.create.product import ProductView
        gui = ProductView(self)
        gui.Show()
