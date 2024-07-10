# main.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from gui.gui_functions import GUIFunctions  # Updated import
from gui.gui import GUI
from gui.menu_config import menu_structure


def generate_actions(menu_structure):
    actions = {}

    def action_template(action_name):
        def action():
            print(f"{action_name} action triggered")

        return action

    for item in menu_structure:
        if item["submenus"]:
            for submenu in item["submenus"]:
                actions[submenu["action"]] = action_template(submenu["action"])
        else:
            actions[item["action"]] = action_template(item["action"])

    # Add exit action
    actions["exit"] = lambda: print("Exit action triggered")

    return actions


def main():
    # Generate actions dynamically based on the menu structure
    actions = generate_actions(menu_structure)

    # Instantiate GUIFunctions with actions
    gui_functions = GUIFunctions(actions)

    # Setup and run the GUI application
    QApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)
    app = QApplication(sys.argv)
    app.setStyle("FUSION")

    # Create and show the main window
    main_window = GUI(actions, gui_functions)
    main_window.show()

    # Start the application event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()




