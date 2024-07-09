# app_functions.py

from gui.menu_config import menu_structure


class AppFunctions:
    def __init__(self):
        self.actions = self.create_actions()

    def create_actions(self):
        actions = {}
        for item in menu_structure:
            if item["submenus"]:
                for submenu in item["submenus"]:
                    action_name = submenu["action"]
                    actions[action_name] = self.create_action_method(action_name)
            else:
                if item["action"] != "exit":
                    action_name = item["action"]
                    actions[action_name] = self.create_action_method(action_name)
        return actions

    def create_action_method(self, action_name):
        def action_method():
            self._log_action(f"{action_name.replace('_', ' ').title()} is running")

        return action_method

    def _log_action(self, message):
        print(message)

    # Explicitly defined methods (if any)
    def confirm_exit(self):
        print("Exit action executed")

# No need to instantiate or generate methods here
