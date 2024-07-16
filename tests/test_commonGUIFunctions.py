import unittest
from PyQt5.QtWidgets import QApplication, QMainWindow
from common_functions import CommonGUIFunctions


class TestCommonGUIFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.widget = QMainWindow()
        self.actions = {
            "action1": lambda: print("Action 1 executed"),
            "action2": lambda: print("Action 2 executed"),
        }
        self.menu_structure = [
            {"name": "File", "action": "file", "submenus": [
                {"name": "Open", "action": "action1"},
                {"name": "Save", "action": "action2"},
            ]},
            {"name": "Edit", "action": "edit", "submenus": []},
        ]
        self.common_funcs = CommonGUIFunctions(self.actions)

    def test_create_action(self):
        action = self.common_funcs.create_action(self.widget, "Test Action", self.actions["action1"])
        self.assertEqual(action.text(), "Test Action")
        self.assertTrue(action.triggered)

    def test_create_action_no_function(self):
        action = self.common_funcs.create_action(self.widget, "Test Action", None)
        self.assertEqual(action.text(), "Test Action")
        self.assertFalse(action.triggered)

    def test_create_actions_map(self):
        actions_map = self.common_funcs.create_actions_map(self.menu_structure, self.widget)
        self.assertIn("action1", actions_map)
        self.assertIn("action2", actions_map)
        self.assertIn("exit", actions_map)

    def test_create_action_method(self):
        action_method = self.common_funcs.create_action_method("action1")
        self.assertTrue(callable(action_method))

    def test_generate_action_methods(self):
        actions_map = self.common_funcs.create_actions_map(self.menu_structure, self.widget)

        class Dummy:
            pass

        obj = Dummy()
        self.common_funcs.generate_action_methods(actions_map, obj)
        self.assertTrue(hasattr(obj, "action1"))
        self.assertTrue(hasattr(obj, "action2"))
        self.assertTrue(hasattr(obj, "exit"))

    def test_create_menus(self):
        actions_map = self.common_funcs.create_actions_map(self.menu_structure, self.widget)
        menu_bar = self.common_funcs.create_menus(self.widget, self.menu_structure, actions_map)
        self.assertEqual(menu_bar.actions()[0].text(), "File")
        self.assertEqual(menu_bar.actions()[1].text(), "Edit")

    def test_notify_click(self):
        with self.assertLogs() as log:
            self.common_funcs.notify_click("action1", self.actions["action1"])
            self.assertIn("action1 menu item clicked", log.output[0])

    def test_setup_window(self):
        self.common_funcs.setup_window(self.widget)
        self.assertEqual(self.widget.windowTitle(), "Investment Tracker")
        self.assertEqual(self.widget.geometry().getRect(), (100, 100, 800, 600))

    def test_confirm_exit(self):
        with self.assertLogs() as log:
            self.common_funcs.confirm_exit(self.widget)
            self.assertIn("Exit menu item clicked", log.output[0])


if __name__ == '__main__':
    unittest.main()
