# create_gui_functions.py

# create_gui_functions.py

from PyQt5.QtWidgets import QAction, QApplication
from PyQt5.QtCore import Qt
from gui.gui import GUI
import sys


class MenuHelper:
    def __init__(self):
        pass

    def create_action(self, widget, name, function):
        """Create an action and connect it to a function."""
        action = QAction(name, widget)
        if function is not None:
            action.triggered.connect(function)
        else:
            print(f"Function for {name} action is not defined.")
        return action

    def create_menus(self, widget, menu_structure, actions_map):
        """Create menus and submenus dynamically."""
        menu_bar = widget.menuBar()
        for item in menu_structure:
            if 'submenus' in item:
                menu = menu_bar.addMenu(item["name"])
                for submenu in item['submenus']:
                    method = getattr(widget, submenu["method_name"], None)
                    action = self.create_action(widget, submenu["name"], method)
                    menu.addAction(action)
            else:
                method = getattr(widget, item["method_name"], None)
                action = self.create_action(widget, item["name"], method)
                menu_bar.addAction(action)
        return menu_bar

    def setup_gui(self, actions):
        """Run the application."""
        QApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)
        application = QApplication(sys.argv)
        application.setStyle("FUSION")
        app_window = GUI(actions)
        app_window.show()
        sys.exit(application.exec_())

    def notify_click(self, menu_item, callback=None):
        """Notify main.py about the menu item clicked."""
        print(f"{menu_item} menu item clicked")
        if callback:
            callback()
        return menu_item

    def setup_window(self, widget):
        """Set up the main window."""
        widget.setWindowTitle("Investment Tracker")
        widget.setGeometry(100, 100, 800, 600)
