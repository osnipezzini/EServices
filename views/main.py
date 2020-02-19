from core import get_icon
from core.license import License
from ui.main_ui import MainUi


class MainView(MainUi):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.SetIcon(get_icon())
        self.SetSize((800, 600))
        self.Maximize()
        self.Centre()
        lic = License().load()
        self.status_bar.SetStatusText(f"Software registrado para : {lic.Company}")


    def open_client(self, event):
        from views.create.client import ClientView
        gui = ClientView(self)

        gui.Show()

    def open_product(self, event):
        from views.create.product import ProductView
        gui = ProductView(self)
        gui.Show()
