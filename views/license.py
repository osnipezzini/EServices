from core import *
from ui.license_ui import LicenseUI

__all__ = ['LicenseView']


class LicenseView(LicenseUI):
    def __init__(self, parent=None):
        super(LicenseView, self).__init__(parent)
        self.SetIcon(get_icon())
