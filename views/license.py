from core import *
from core.license import License
from ui.license_ui import LicenseUI

__all__ = ['LicenseView']

license = License()


class LicenseView(LicenseUI):
    def __init__(self, parent=None):
        super(LicenseView, self).__init__(parent)
        self.SetIcon(get_icon())
        import socket
        machine = socket.gethostname()
        if len(self.text_machine.GetValue()) == 0:
            self.text_machine.SetValue(machine)
        if len(self.text_serial.GetValue()) == 0:
            key = license.generate()
            self.text_serial.SetValue(key)

    def get_license(self, event):
        machine = self.text_machine.GetValue()
        cpf = self.text_ident.GetValue()
        password = self.text_password.GetValue()
        ret, name = license.get(machine, cpf, password)
        import wx
        if ret:
            wx.MessageBox('Sistema registrado com sucesso para : ' + name, 'Sucesso')
            self.EndModal(wx.OK)
        else:
            wx.MessageBox('Ocorreu o seguinte erro ao registrar o sistema :\n' + name,
                          'Error', style=wx.ICON_ERROR)
