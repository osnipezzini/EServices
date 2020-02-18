import wx

from core import get_icon
from core.config import Config
from ui.config_ui import ConfigUI

config = Config()


class ConfigView(ConfigUI):
    def __init__(self, parent=None):
        super(ConfigView, self).__init__(parent)
        self.SetIcon(get_icon())

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

        cfg = dict(host=host, port=port, name=name, user=user, password=password)
        config.save(cfg)
        wx.MessageBox('Configurações salvas !', 'Sucesso', style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION)
