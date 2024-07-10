# gui/gui.py

from PyQt5.QtWidgets import QMainWindow
from .menu_config import menu_structure
from .styling import set_styling


class GUI(QMainWindow):
    def __init__(self, actions, gui_functions):
        super().__init__()
        self.actions = actions
        self.gui_functions = gui_functions
        print("Main menu created")

        self.actions_map = self.gui_functions.create_actions_map(menu_structure, self)
        self.gui_functions.setup_window(self)
        self.menu_bar = self.gui_functions.create_menus(self, menu_structure, self.actions_map)
        self.setMenuBar(self.menu_bar)
        set_styling(self)

        self.gui_functions.generate_action_methods(self.actions_map, self)
