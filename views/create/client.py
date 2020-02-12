import wx

from core import get_icon
from ui.client_ui import ClientForm, ClientSearch


class ClientView(ClientForm):
    def __init__(self, parent=None):
        super(ClientView, self).__init__(parent)
        self.SetIcon(get_icon())


    def search_client( self, event ):
        search = ClientSearchView(self)
        if search.ShowModal() == wx.OK:
            print('OK')

class ClientSearchView(ClientSearch):
    def __init__(self, parent):
        super(ClientSearchView, self).__init__(parent)
        self.SetIcon(get_icon())
        self.data_search.ClearColumns()
        self.data_search.DeleteAllItems()
        self.data_search.AppendTextColumn('Grid', flags=wx.COL_HIDDEN)
        self.data_search.AppendTextColumn('Código')
        self.data_search.AppendTextColumn('Nome', flags=wx.COL_RESIZABLE, width=200, align=wx.ALIGN_CENTER)
        self.data_search.AppendTextColumn('CPF/CNPJ')
        self.text_search.SetFocus()

    def process_keys(self, event):
        evt = event.GetKeyCode()
        import wx
        if evt == wx.WXK_NUMPAD_ENTER or evt == wx.WXK_RETURN:
            self.search_client(event)

    def search_client(self, event):
        from services.client import Client
        text = self.text_search.GetValue()
        q = Client()
        result = q.search(text)
        print(result)
        for r in result:
            self.data_search.AppendItem([r.grid, r.code, r.name, r.doc])

