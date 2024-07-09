# main.py

from db.create_db import DatabaseManager
from gui.gui_functions import GUIFunctions
from app_functions import AppFunctions


class MainApp:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.app_functions = AppFunctions()
        self.gui_functions = GUIFunctions()

    def menu_item_callback(self, menu_item):
        menu_action = self.app_functions.actions.get(menu_item)
        if menu_action:
            menu_action()

    def run(self):
        self.gui_functions.setup_gui(self.app_functions.actions, self.menu_item_callback)


if __name__ == "__main__":
    app = MainApp()
    app.run()
