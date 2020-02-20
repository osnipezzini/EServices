import wx

from core import get_icon
from core.config import Config
from ui.config_ui import ConfigUI

config = Config()


class ConfigView(ConfigUI):
    def __init__(self, parent=None):
        super(ConfigView, self).__init__(parent)
        self.SetIcon(get_icon())
        if config.load():
            self.text_db_host.SetValue(config.db_host)
            self.text_db_port.SetValue(config.db_port)
            self.text_db_name.SetValue(config.db_name)
            self.text_db_username.SetValue(config.db_user)
            self.text_db_password.SetValue(config.db_password)

    def save_cfg(self, event):

        host = self.text_db_host.GetValue()
        port = self.text_db_port.GetValue()
        name = self.text_db_name.GetValue()
        user = self.text_db_username.GetValue()
        password = self.text_db_password.GetValue()
        if len(host) == 0:
            host = 'localhost'
        if len(port) == 0:
            port = '5432'
        if len(name) == 0:
            name = 'eservices'
        if len(user) == 0:
            user = 'postgres'

        cfg = dict(host=host, port=port, name=name, user=user, password=password, driver='PostgreSQL')
        config.save(cfg)
        self.fill_form(cfg)
        if wx.MessageBox('Configurações salvas !', 'Sucesso', style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION):
            self.Destroy()

    def fill_form(self, data):
        if 'user' in data:
            self.text_db_username.SetValue(data['user'])
        if 'port' in data:
            self.text_db_port.SetValue(data['port'])
        if 'name' in data:
            self.text_db_name.SetValue(data['name'])
        if 'password' in data:
            self.text_db_password.SetValue(data['password'])
        if 'host' in data:
            self.text_db_host.SetValue(data['host'])