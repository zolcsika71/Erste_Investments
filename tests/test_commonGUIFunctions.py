# tests/test_commonGUIFunctions.py

import pytest
from gui.common_functions import CommonGUIFunctions
from gui.gui_functions import GUIFunctions


class TestCommonGUIFunctions:
    def setup_method(self):
        actions = {}  # You can define any necessary actions here
        self.gui_functions = GUIFunctions(actions)

    def test_create_action(self):
        # Example test case
        action = self.gui_functions.create_action(None, "Test Action", None)
        assert action.text() == "Test Action"
