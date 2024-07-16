import sys
from PyQt5.QtWidgets import QApplication
from gui.common_functions import CommonGUIFunctions


class TestCommonGUIFunctions:

    @classmethod
    def set_up_class(cls):
        cls.app = QApplication(sys.argv)  # Ensure QApplication is created
        cls.gui_functions = CommonGUIFunctions(actions={})

    def test_create_action(self):
        # Example test case
        action = self.gui_functions.create_action(None, "Test Action", None)
        assert action.text() == "Test Action"

