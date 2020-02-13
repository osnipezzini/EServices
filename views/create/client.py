import wx

from core import get_icon
from ui.client_ui import ClientForm, ClientSearch
from services.client import Client


class ClientView(ClientForm):
    def __init__(self, parent=None):
        super(ClientView, self).__init__(parent)
        self.SetIcon(get_icon())
        self.client = None
        self.new_client(None)

    def search_client(self, event):
        search = ClientSearchView(self)
        if search.ShowModal() == wx.OK:
            print('OK')

    def get_zip_code( self, event ):
        cep = self.text_zipcode.GetValue()
        from elibs.utils import dict_to_prop
        from elibs.utils import get_cep
        res = get_cep(cep)
        result = dict_to_prop(res)
        self.text_zipcode.SetValue(result.cep)
        self.text_address.SetValue(result.logradouro)
        self.text_district.SetValue(result.bairro)
        self.text_city_name.SetValue(result.localidade)
        self.text_state.SetValue(result.uf)
        self.text_city_code.SetValue(result.ibge)
        self.text_country_name.SetValue('Brasil')
        self.text_address_nr.SetFocus()



    def save_client(self, event):
        pass

    def new_client(self, event):
        self.client = None
        from models import Person
        code = Person().get_seq()
        self.text_code.SetValue(str(code))
        self.text_doc.SetValue('')
        self.text_name.SetValue('')
        self.text_group_grid.SetValue('2')
        self.text_group_name.SetValue('CLIENTES')
        self.text_zipcode.SetValue('')
        self.text_address.SetValue('')
        self.text_district.SetValue('')
        self.text_city_name.SetValue('')
        self.text_state.SetValue('')
        self.text_city_code.SetValue('')
        self.text_country_name.SetValue('Brasil')
        self.text_doc.SetFocus()

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
