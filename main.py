import wx

from core import *
from views.main import MainView


def main():
    from core.license import License
    if License().check():
        from core.config import Config
        if Config().check():
            widget = MainView()
            widget.Show()
        else:
            from views.config import ConfigView
            widget = ConfigView()
            widget.Show()
    else:
        from views.license import LicenseView
        widget = LicenseView()
        if widget.ShowModal() == wx.OK:
            main()
        else:
            app.Destroy()


if __name__ == '__main__':
    app = BaseApp()
    main()
    app.MainLoop()
