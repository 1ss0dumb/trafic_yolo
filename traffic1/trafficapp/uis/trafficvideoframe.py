from PyQt5.QtWidgets import QDialog
from trafficapp.uis.videoui import Ui_Video

class WTrafficVideoDialog(QDialog):
    def __init__(self, parent=None):
        super(WTrafficVideoDialog, self).__init__(parent)
        self.ui = Ui_Video()
        self.ui.setupUi(self)
