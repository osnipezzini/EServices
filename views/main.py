from core import get_icon
from models import DBSession, Product
from ui.main_ui import MainUi
from elibs import MainWindow


class MainView(MainUi):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.SetIcon(get_icon())

        from models.person import Person

        session = DBSession()

        # # Insert a Person in the person table
        new_person = Person(name='Osni Pezzini Jr', email='teste@teste.com', doc='000.000.000-00')
        session.add(new_person)
        session.commit()
        #
        product = Product(barcode='0000021212', name='Produto teste', price=10.0, person=new_person)
        session.add(product)
        session.commit()
        for user, product in session.query(Person, Product):
            print(product.person)

    def open_client( self, event ):
        from views.create.client import ClientView
        gui = ClientView(self)

        gui.Show()
