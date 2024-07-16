# main.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from gui.gui_functions import GUIFunctions
from gui.gui import GUI
from gui.menu_config import menu_structure
from app_functions import generate_actions  # Import the function


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
