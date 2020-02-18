import wx

from core import *
from views.main import MainView


def main():
    from core.license import License
    from core import is_debug
    if License().check() or is_debug():
        from core.config import Config
        if Config().check() or is_debug():
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
    import os

    os.environ['HASH_KEY'] = '81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs='

    main()
    app.MainLoop()
