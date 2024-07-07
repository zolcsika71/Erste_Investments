import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox, QMenu, QMenuBar, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


def run_app():
    """Run the application."""
    QApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)
    application = QApplication(sys.argv)
    application.setStyle("FUSION")
    app_window = InvestmentTracker()
    app_window.show()
    sys.exit(application.exec_())


class InvestmentTracker(QMainWindow):
    def __init__(self):
        """
        Initialize the InvestmentTracker class.
        Sets up the main window, creates menu bar and defines instance attributes.
        Calls methods to create actions, setup menus, set the menu bar, and apply styling.
        """
        super().__init__()
        self.setup_window()
        print("Main menu created")

        self.menu_bar = QMenuBar(self)

        # Define instance attributes
        self.import_action = None
        self.current_action = None
        self.sell_buy_action = None
        self.suggested_action = None
        self.service_menu = None
        self.display_menu = None
        self.exit_action = None
        self.import_current_action = None
        self.delete_recreate_action = None

        self.create_actions()
        self.setup_menus()
        self.setMenuBar(self.menu_bar)

        self.set_styling()

    def setup_window(self):
        self.setWindowTitle("Investment Tracker")
        self.setGeometry(100, 100, 800, 600)

    def create_actions(self):
        self.import_action = self.create_action("Import Suggested Portfolio", self.import_suggested_portfolio)
        self.current_action = self.create_action("Current Portfolio", self.show_current_portfolio)
        self.sell_buy_action = self.create_action("Sell & Buy on Current Portfolio", self.show_sell_buy)
        self.suggested_action = self.create_action("Suggested Portfolio", self.show_suggested_portfolio)
        self.delete_recreate_action = self.create_action("Delete and Recreate DB", self.delete_recreate_db)
        self.import_current_action = self.create_action("Import Current Portfolio", self.import_current_portfolio)
        self.exit_action = self.create_action("Exit", self.confirm_exit)

    # noinspection PyUnresolvedReferences
    def create_action(self, name, function):
        action = QAction(name, self)
        action.triggered.connect(function)
        return action

    def setup_menus(self):
        self.menu_bar.addAction(self.import_action)
        self.display_menu = self.create_menu("Display",
                                             [self.current_action, self.sell_buy_action, self.suggested_action])
        self.service_menu = self.create_menu("Service", [self.delete_recreate_action, self.import_current_action])
        self.menu_bar.addAction(self.exit_action)

    def create_menu(self, name, actions):
        menu = QMenu(name, self)
        self.menu_bar.addMenu(menu)
        for action in actions:
            menu.addAction(action)
        return menu

    def set_styling(self):
        self.setStyleSheet("""
            /* Color variables for consistency */
            QMainWindow {
                --background-color: #f7f7f7;
                --text-color: #333333;
                --border-color: #dcdcdc;
                --hover-background-color: #f0f0f0;
                --pressed-background-color: #e6e6e6;

                background-color: var(--background-color); /* Light gray background */
                font-family: Arial, Helvetica, sans-serif;
            }

            QMenuBar {
                background-color: #ffffff; /* White background */
                color: var(--text-color); /* Dark gray text */
                padding: 5px;
                border-bottom: 1px solid var(--border-color); /* Light gray border */
            }

            QMenuBar::item {
                background-color: #ffffff; /* White background */
                color: var(--text-color); /* Dark gray text */
                padding: 5px 10px;
                margin: 0 5px;
                border-radius: 4px;
            }

            QMenuBar::item::selected {
                background-color: var(--hover-background-color); /* Light gray for selected item */
            }

            QMenu {
                background-color: #ffffff; /* White background */
                color: var(--text-color); /* Dark gray text */
                border: 1px solid var(--border-color); /* Light gray border */
                border-radius: 4px;
            }

            QMenu::item {
                padding: 5px 10px;
            }

            QMenu::item::selected {
                background-color: var(--pressed-background-color); /* Slightly darker gray for selected item */
            }

            QAction {
                color: var(--text-color); /* Dark gray text */
            }

            QPushButton {
                background-color: #ffffff; /* White background */
                color: var(--text-color); /* Dark gray text */
                padding: 8px 16px;
                border: 1px solid var(--border-color); /* Light gray border */
                border-radius: 4px;
                margin: 5px;
            }

            QPushButton:hover {
                background-color: var(--hover-background-color); /* Light gray on hover */
            }

            QPushButton:pressed {
                background-color: var(--pressed-background-color); /* Slightly darker gray when pressed */
            }
        """)

    def import_suggested_portfolio(self):
        print("Import Suggested Portfolio menu item added")
        pass

    def show_current_portfolio(self):
        print("Current Portfolio menu item clicked")
        pass

    def show_sell_buy(self):
        print("Sell & Buy on Current Portfolio menu item clicked")
        pass

    def show_suggested_portfolio(self):
        print("Suggested Portfolio menu item clicked")
        pass

    def delete_recreate_db(self):
        print("Delete and Recreate DB menu item clicked")
        pass

    def import_current_portfolio(self):
        print("Import Current Portfolio menu item clicked")
        pass

    def confirm_exit(self):
        print("Exit menu item clicked")
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()


if __name__ == "__main__":
    run_app()
