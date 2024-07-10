# app_functions.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QMessageBox


class GUIFunctions:
    def __init__(self, actions):
        self.actions = actions
        self.parent = None  # Initialize parent attribute

    def create_action(self, widget, name, function):
        action = QAction(name, widget)
        if function is not None:
            action.triggered.connect(function)
        else:
            print(f"Function for {name} action is not defined.")
        return action

    def create_actions_map(self, menu_structure):
        actions_map = {}
        for item in menu_structure:
            if item["submenus"]:
                for submenu in item["submenus"]:
                    actions_map[submenu["action"]] = self.create_action_method(submenu["action"])
            else:
                actions_map[item["action"]] = self.create_action_method(item["action"])

        # Ensure "exit" action is included
        actions_map["exit"] = lambda: self.confirm_exit()
        return actions_map

    def create_action_method(self, action_name):
        def action_method():
            self.notify_click(action_name, self.actions.get(action_name))
        return action_method

    def generate_action_methods(self, actions_map, obj):
        for action in actions_map.keys():
            if not hasattr(obj, action):
                setattr(obj, action, actions_map[action])

    def create_menus(self, widget, menu_structure, actions_map):
        menu_bar = widget.menuBar()
        for item in menu_structure:
            if item['submenus']:
                menu = menu_bar.addMenu(item["name"])
                for submenu in item['submenus']:
                    method = actions_map.get(submenu["action"], None)
                    action = self.create_action(widget, submenu["name"], method)
                    menu.addAction(action)
            else:
                method = actions_map.get(item["action"], None)
                action = self.create_action(widget, item["name"], method)
                menu_bar.addAction(action)
        return menu_bar

    def setup_gui(self, actions, callback):
        QApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)
        application = QApplication(sys.argv)
        application.setStyle("FUSION")
        app_window = GUI(actions, self)
        self.parent = app_window  # Set the main window as the parent
        app_window.show()
        sys.exit(application.exec_())

    def notify_click(self, menu_item, callback=None):
        print(f"{menu_item} menu item clicked")
        if callback:
            callback()
        return menu_item

    def setup_window(self, widget):
        widget.setWindowTitle("Investment Tracker")
        widget.setGeometry(100, 100, 800, 600)

    def confirm_exit(self):
        print("Exit menu item clicked")
        reply = QMessageBox.question(
            self.parent, 'Exit', 'Are you sure you want to exit?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()

