import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QMessageBox
)
from PyQt5.QtCore import Qt

from .menu_config import menu_structure
from .styling import set_styling
from .menu_helper import create_menus


def setup_gui(actions):
    """Run the application."""
    QApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)
    application = QApplication(sys.argv)
    application.setStyle("FUSION")
    app_window = GUI(actions)
    app_window.show()
    sys.exit(application.exec_())


def notify_click(menu_item, callback=None):
    """Notify main.py about the menu item clicked."""
    print(f"{menu_item} menu item clicked")
    if callback:
        callback()
    return menu_item


class GUI(QMainWindow):
    def __init__(self, actions):
        super().__init__()
        self.actions = actions
        self.setup_window()
        print("Main menu created")

        self.actions_map = {
            "import_suggested_portfolio": self.import_suggested_portfolio,
            "show_current_portfolio": self.show_current_portfolio,
            "sell_buy_on_current_portfolio": self.show_sell_buy,
            "show_suggested_portfolio": self.show_suggested_portfolio,
            "delete_and_recreate_db": self.delete_recreate_db,
            "import_current_portfolio": self.import_current_portfolio,
            "exit": self.confirm_exit,
        }

        self.menu_bar = create_menus(self, menu_structure, self.actions_map)
        self.setMenuBar(self.menu_bar)
        set_styling(self)

    def setup_window(self):
        """Set up the main window."""
        self.setWindowTitle("Investment Tracker")
        self.setGeometry(100, 100, 800, 600)

    def import_suggested_portfolio(self):
        """Handle the import suggested portfolio action."""
        notify_click('import_suggested_portfolio', self.actions['import_suggested_portfolio'])

    def show_current_portfolio(self):
        """Handle the show current portfolio action."""
        notify_click('show_current_portfolio', self.actions['show_current_portfolio'])

    def show_sell_buy(self):
        """Handle the show sell & buy action."""
        notify_click('sell_buy_on_current_portfolio', self.actions['sell_buy_on_current_portfolio'])

    def show_suggested_portfolio(self):
        """Handle the show suggested portfolio action."""
        notify_click('show_suggested_portfolio', self.actions['show_suggested_portfolio'])

    def delete_recreate_db(self):
        """Handle the delete and recreate DB action."""
        notify_click('delete_recreate_db', self.actions['delete_recreate_db'])

    def import_current_portfolio(self):
        """Handle the import current portfolio action."""
        notify_click('import_current_portfolio', self.actions['import_current_portfolio'])

    def confirm_exit(self):
        """Handle the exit action."""
        print("Exit menu item clicked")
        reply = QMessageBox.question(
            self, 'Exit', 'Are you sure you want to exit?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()
