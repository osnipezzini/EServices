import wx

from core import get_icon, log
from services.client import ClientService
from ui.client_ui import ClientForm, ClientSearch, SearchOptions


class ClientView(ClientForm):
    def __init__(self, parent=None):
        super(ClientView, self).__init__(parent)
        self.SetIcon(get_icon())
        self.client = None
        self.new_client(None)

    def search_client(self, event):
        search = ClientSearchView(self)
        if search.ShowModal() == wx.OK:
            self.model_to_fields(search.model)

    def search_group(self, event):
        from views.create.groups import PersonGroupSearch
        search = PersonGroupSearch(self)
        search.search(None)
        if search.ShowModal() == wx.OK:
            self.text_group_name.SetValue(search.model.name)
            self.text_group_grid.SetValue(str(search.model.code))

    def model_to_fields(self, model):
        self.client = model.grid
        self.text_code.SetValue(str(model.code))
        self.text_doc.SetValue(model.doc)
        self.text_name.SetValue(model.name)
        self.text_group_grid.SetValue('2')
        self.text_group_name.SetValue('CLIENTES')
        self.text_zipcode.SetValue(model.zipcode)
        self.text_address.SetValue(model.address)
        self.text_address_nr.SetValue(model.address_nr)
        self.text_district.SetValue(model.district)
        self.text_city_name.SetValue(model.city_name)
        self.text_state.SetValue(model.state)
        self.text_city_code.SetValue(model.city_code)
        self.text_country.SetValue(model.country)
        self.check_active.SetValue((True))
        if model.flag == 'I':
            self.check_active.SetValue(False)
        self.text_doc.SetFocus()

    def get_zip_code(self, event):
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
        self.text_country.SetValue('Brasil')
        self.text_address_nr.SetFocus()

    def fields_to_obj(self, ignore_fields=[]):
        client = dict()
        for k, v in self.__dict__.items():
            if k.startswith('check_'):
                val = v.GetValue()
                if val:
                    client['flag'] = 'A'
                else:
                    client['flag'] = 'I'
            if k.startswith('text_'):
                key = k[5:]
                if key not in ignore_fields:
                    client[key] = v.GetValue()
        return client

    def save_client(self, event):
        try:
            client = ClientService()
            client.update(self.client, self.fields_to_obj(['group_grid', 'group_name', 'country_name']))
            wx.MessageBox('Salvo com sucesso !', style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION, caption='Atualizado')
        except Exception as e:
            log.debug(e)
            wx.MessageBox(
                'Ocorreu um erro ao salvar as configurações .\nConsulte o arquivo de log para mais detalhes.',
                style=wx.OK | wx.CENTRE | wx.ICON_ERROR, caption='Erro interno'
            )

    def new_client(self, event):
        self.client = None
        from services.client import ClientService
        cl = ClientService()
        code = cl.get_next_code()
        self.check_active.SetValue(True)
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
        self.text_country.SetValue('Brasil')
        self.text_doc.SetFocus()

    def delete_client(self, event):
        if self.client is not None:
            q = ClientService()
            q.delete(self.client)
            self.new_client(None)


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
        self.search_options = ['A']
        self.model = -1

    def process_keys(self, event):
        event.Skip()

    def search_client(self, event):
        text = self.text_search.GetValue()
        choice = self.choice_search_type.GetStringSelection()
        q = ClientService()
        result = q.search(text, choice, self.search_options)
        self.data_search.DeleteAllItems()
        for r in result:
            self.data_search.AppendItem([r.grid, r.code, r.name, r.doc])

    def load_client(self, event):
        row = self.data_search.GetSelectedRow()
        grid = self.data_search.GetValue(row, 0)
        q = ClientService()
        self.model = q.get(grid)
        self.EndModal(wx.OK)

    def open_options(self, event):
        options = SearchOptionsView(self, self.search_options)
        if options.ShowModal() == wx.OK:
            self.search_options = options.options


class SearchOptionsView(SearchOptions):
    def __init__(self, parent, options=['A']):
        super(SearchOptionsView, self).__init__(parent)
        self.options = options
        if 'D' in self.options:
            self.check_deleted.SetValue(True)
        if 'I' in self.options:
            self.check_inactived.SetValue(True)

    def save_options(self, event):
        if self.check_deleted.IsChecked() and 'D' not in self.options:
            self.options.append('D')
        if self.check_inactived.IsChecked() and 'I' not in self.options:
            self.options.append('I')
        self.EndModal(wx.OK)
