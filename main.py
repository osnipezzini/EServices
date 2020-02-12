import sys
from core import *
from elibs import *
from views.main import MainView

if __name__ == '__main__':
    app = BaseApp()
    widget = MainView()
    widget.Show()
    app.MainLoop()
