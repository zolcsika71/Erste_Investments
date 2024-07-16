# common_functions.py

from PyQt5.QtWidgets import QAction, QApplication, QMessageBox


# noinspection PyUnresolvedReferences
class CommonGUIFunctions:
    def __init__(self, actions):
        self.actions = actions
        self.parent = None

    @staticmethod
    def create_action(widget, name, function):
        action = QAction(name, widget)
        if function is not None:
            action.triggered.connect(function)
        else:
            print(f"Function for {name} action is not defined.")
        return action

    def create_actions_map(self, menu_structure, parent=None):
        self.parent = parent
        actions_map = {}
        for item in menu_structure:
            if item["submenus"]:
                for submenu in item["submenus"]:
                    actions_map[submenu["action"]] = self.create_action_method(submenu["action"])
            else:
                actions_map[item["action"]] = self.create_action_method(item["action"])

        # Ensure "exit" action is included
        actions_map["exit"] = lambda: self.confirm_exit(self.parent)
        return actions_map

    def create_action_method(self, action_name):
        def action_method():
            self.notify_click(action_name, self.actions.get(action_name))

        return action_method

    @staticmethod
    def generate_action_methods(actions_map, obj):
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

    @staticmethod
    def notify_click(menu_item, callback=None):
        print(f"{menu_item} menu item clicked")
        if callback:
            callback()
        return menu_item

    @staticmethod
    def setup_window(widget):
        widget.setWindowTitle("Investment Tracker")
        widget.setGeometry(100, 100, 800, 600)

    @staticmethod
    def confirm_exit(parent):
        print("Exit menu item clicked")
        reply = QMessageBox.question(
            parent, 'Exit', 'Are you sure you want to exit?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()
