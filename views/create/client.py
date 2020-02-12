import wx

from core import get_icon
from ui.client_ui import ClientForm, ClientSearch
from services.client import Client


class ClientView(ClientForm):
    def __init__(self, parent=None):
        super(ClientView, self).__init__(parent)
        self.SetIcon(get_icon())
        self.client = None

    def search_client(self, event):
        search = ClientSearchView(self)
        if search.ShowModal() == wx.OK:
            print('OK')

    def save_client(self, event):
        pass

    def new_client(self, event):
        pass

    def delete_client(self, event):
        if self.text_name.GetValue() != '':
            grid = int(self.text_name.GetValue())
            self.client = grid
        if self.client is None:
            from core.ui import MessageBox
            dlg = MessageBox(self, 'Necessário preencher todos os campos')
            dlg.SetExtendedMessage('Verificado que não foi preenchido o campo do cliente , favor preencher')
            dlg.SetWindowStyle(wx.ICON_ERROR)
            dlg.ShowModal()
        else:
            q = Client()
            delete = q.delete(self.client)
            print(delete)


class ClientSearchView(ClientSearch):
    def __init__(self, parent):
        super(ClientSearchView, self).__init__(parent)
        self.SetIcon(get_icon())
        self.data_search.ClearColumns()
        self.data_search.DeleteAllItems()
        self.data_search.AppendTextColumn('Grid', flags=wx.COL_HIDDEN)
        self.data_search.AppendTextColumn('Código', width=80)
        self.data_search.AppendTextColumn('Nome', width=190, align=wx.ALIGN_CENTER)
        self.data_search.AppendTextColumn('CPF/CNPJ', width=190, align=wx.ALIGN_CENTER)
        self.text_search.SetFocus()

    def process_keys(self, event):
        evt = event.GetKeyCode()
        import wx
        if evt == wx.WXK_NUMPAD_ENTER or evt == wx.WXK_RETURN:
            self.search_client(event)

    def search_client(self, event):
        text = self.text_search.GetValue()
        choice = self.choice_search_type.GetStringSelection()
        q = Client()
        result = q.search(text, choice)
        self.data_search.DeleteAllItems()
        for r in result:
            self.data_search.AppendItem([r.grid, r.code, r.name, r.doc])
