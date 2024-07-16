# gui_functions.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from .gui import GUI
from .common_functions import CommonGUIFunctions


class GUIFunctions(CommonGUIFunctions):
    def __init__(self, actions):
        super().__init__(actions)

    def setup_gui(self, actions):
        QApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)
        application = QApplication(sys.argv)
        application.setStyle("FUSION")
        app_window = GUI(actions, self)
        self.parent = app_window
        app_window.show()
        sys.exit(application.exec_())
