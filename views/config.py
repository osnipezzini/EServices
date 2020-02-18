from core import get_icon
from ui.config_ui import ConfigUI


class ConfigView(ConfigUI):
    def __init__(self, parent=None):
        super(ConfigView, self).__init__(parent)
        self.SetIcon(get_icon())
