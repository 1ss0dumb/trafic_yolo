from  PyQt5.QtWidgets import QLabel
from  PyQt5.QtCore import pyqtSignal

# 定制标签，实现了clicked信号
class WLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(WLabel, self).__init__(parent)

    def mouseReleaseEvent(self, e):
        self.clicked.emit()

