import wx

from core import log, get_icon
from models import PersonGroup
from services.groups import PersonGroupService
from ui.main_ui import Search
from ui.client_ui import PersonGroupForm, SearchOptions


class PersonGroupView(PersonGroupForm):
    def __init__(self, parent):
        super(PersonGroupView, self).__init__(parent)
        self.grid = -1

    def search_act(self, event):
        search = Search(self)
        if search.ShowModal() == wx.OK:
            print('OK')

    def model_to_fields(self, model: PersonGroup):
        self.check_active.SetValue(True if model.flag == 'A' else False)
        for k, v in model.__dict__.items():
            try:
                prop = 'text_' + k
                self.prop.SetValue(v)
            except Exception as exc:
                log.debug(exc)
        self.grid = model.grid
        self.text_code.SetValue(model.code)


class PersonGroupSearch(Search):
    def __init__(self, parent):
        super(PersonGroupSearch, self).__init__(parent)
        self.SetIcon(get_icon())

        self.data_search.ClearColumns()
        self.data_search.DeleteAllItems()
        self.data_search.AppendTextColumn('Grid', flags=wx.COL_HIDDEN)
        self.data_search.AppendTextColumn('Código', width=80)
        self.data_search.AppendTextColumn('Nome', width=190, align=wx.ALIGN_CENTER)
        self.text_search.SetFocus()
        self.search_options = ['A']
        self.model = PersonGroup

    def process_keys(self, event):
        event.Skip()

    def search(self, event):
        text = self.text_search.GetValue()
        choice = self.choice_search_type.GetStringSelection()
        q = PersonGroupService()
        result = q.search(text, choice, self.search_options)
        self.data_search.DeleteAllItems()
        for r in result:
            self.data_search.AppendItem([r.grid, r.code, r.name])

    def load_client(self, event):
        row = self.data_search.GetSelectedRow()
        grid = self.data_search.GetValue(row, 0)
        q = PersonGroupService()
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
        if self.check_inactived.IsChecked() and 'D' not in self.options:
            self.options.append('I')
        self.EndModal(wx.OK)
