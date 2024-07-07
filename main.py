# imports

from db_scripts.create_db import DatabaseManager
from gui.gui import setup_gui, GUI, notify_click
from db_scripts.modify_db import DBModifier

if __name__ == '__main__':
    db_manager = DatabaseManager()
    db_modifier = DBModifier()

    # Setup GUI with actions
    setup_gui(db_modifier.actions)

    gui_handler = GUI(db_modifier.actions)

    # Define the callback function
    def menu_item_callback(menu_item):
        menu_action = db_modifier.actions.get(menu_item)
        if menu_action:
            menu_action()

    # Example usage with callback:
    for action in db_modifier.actions:
        notify_click(action, menu_item_callback)




