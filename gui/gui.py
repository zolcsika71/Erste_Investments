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

        self.actions_map = {
            "import_suggested_portfolio": self.import_suggested_portfolio,
            "show_current_portfolio": self.show_current_portfolio,
            "sell_buy_on_current_portfolio": self.sell_buy_on_current_portfolio,
            "show_suggested_portfolio": self.show_suggested_portfolio,
            "delete_and_recreate_db": self.delete_recreate_db,
            "import_current_portfolio": self.import_current_portfolio,
            "exit": self.confirm_exit,
        }

        self.gui_functions.setup_window(self)
        self.menu_bar = self.gui_functions.create_menus(self, menu_structure, self.actions_map)
        self.setMenuBar(self.menu_bar)
        set_styling(self)

    def import_suggested_portfolio(self):
        self.gui_functions.notify_click('import_suggested_portfolio', self.actions['import_suggested_portfolio'])

    def show_current_portfolio(self):
        self.gui_functions.notify_click('show_current_portfolio', self.actions['show_current_portfolio'])

    def sell_buy_on_current_portfolio(self):
        self.gui_functions.notify_click('sell_buy_on_current_portfolio', self.actions['sell_buy_on_current_portfolio'])

    def show_suggested_portfolio(self):
        self.gui_functions.notify_click('show_suggested_portfolio', self.actions['show_suggested_portfolio'])

    def delete_recreate_db(self):
        self.gui_functions.notify_click('delete_recreate_db', self.actions['delete_recreate_db'])

    def import_current_portfolio(self):
        self.gui_functions.notify_click('import_current_portfolio', self.actions['import_current_portfolio'])

    def confirm_exit(self):
        print("Exit menu item clicked")
        reply = QMessageBox.question(
            self, 'Exit', 'Are you sure you want to exit?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()
