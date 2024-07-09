# gui/gui.py

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from .menu_config import menu_structure
from .styling import set_styling


class GUI(QMainWindow):
    def __init__(self, actions, gui_functions):
        super().__init__()
        self.actions = actions
        self.gui_functions = gui_functions
        print("Main menu created")

        self.actions_map = self.create_actions_map()
        self.gui_functions.setup_window(self)
        self.menu_bar = self.gui_functions.create_menus(self, menu_structure, self.actions_map)
        self.setMenuBar(self.menu_bar)
        set_styling(self)
        self.generate_action_methods()

    def create_actions_map(self):
        actions_map = {}
        for item in menu_structure:
            if item["submenus"]:
                for submenu in item["submenus"]:
                    actions_map[submenu["action"]] = self.create_action_method(submenu["action"])
            else:
                actions_map[item["action"]] = self.create_action_method(item["action"])

        # Ensure "exit" action is included
        actions_map["exit"] = self.confirm_exit
        return actions_map

    def generate_action_methods(self):
        for action in self.actions_map.keys():
            if not hasattr(self, action):
                setattr(self, action, self.actions_map[action])

    def create_action_method(self, action_name):
        def action_method():
            self.gui_functions.notify_click(action_name, self.actions[action_name])

        return action_method

    # Static exit function
    def confirm_exit(self):
        print("Exit menu item clicked")
        reply = QMessageBox.question(
            self, 'Exit', 'Are you sure you want to exit?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()

# No need to instantiate or generate methods here
