import wx

from core import *
from views.main import MainView


def main():
    from core.license import License
    from core import is_debug
    if License().check() or is_debug():
        from core.config import Config
        if Config().check() or is_debug():
            app = BaseApp()
            widget = MainView()
            widget.Show()
            app.MainLoop()
        else:
            from views.config import ConfigView
            app = wx.App()
            widget = ConfigView()
            widget.Show()
            app.MainLoop()
    else:
        from views.license import LicenseView
        app = wx.App()
        widget = LicenseView()
        if widget.ShowModal() == wx.OK:
            main()
        else:
            app.Destroy()


if __name__ == '__main__':
    import os

    os.environ['HASH_KEY'] = '81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs='
    main()
