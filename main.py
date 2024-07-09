# main.py

from gui.gui_functions import GUIFunctions
from db.create_db import DatabaseManager
from app_functions import AppFunctions


class MainApp:
    """Main application class."""

    def __init__(self):
        """Initialize the main application."""
        self.database = DatabaseManager()
        self.app_functions = AppFunctions()
        self.gui_functions = GUIFunctions()

    def run(self):
        """Run the main application."""
        self.gui_functions.setup_gui(
            self.app_functions.actions,
            self.menu_item_callback
        )

    def menu_item_callback(self):
        """Callback function for menu items."""
        print("Menu item callback executed")


if __name__ == "__main__":
    app = MainApp()
    app.run()
