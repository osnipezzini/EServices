import wx

from core import get_icon


class MessageBox(wx.GenericMessageDialog):
    def __init__(self, parent, message, caption='Informação', style=wx.OK | wx.CENTRE | wx.ICON_INFORMATION,
                 pos=wx.DefaultPosition):
        super(MessageBox, self).__init__(parent, message, caption, style, pos)
        self.SetIcon(get_icon())
