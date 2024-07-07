# menu_helper.py

from PyQt5.QtWidgets import QAction


def create_action(widget, name, function):
    """Create an action and connect it to a function."""
    action = QAction(name, widget)
    if function is not None:
        action.triggered.connect(function)
    else:
        print(f"Function for {name} action is not defined.")
    return action


def create_menus(widget, menu_structure, actions_map):
    """Create menus and submenus dynamically."""
    menu_bar = widget.menuBar()
    for item in menu_structure:
        if 'submenus' in item:
            menu = menu_bar.addMenu(item["name"])
            for submenu in item['submenus']:
                method = getattr(widget, submenu["method_name"], None)
                action = create_action(widget, submenu["name"], method)
                menu.addAction(action)
        else:
            method = getattr(widget, item["method_name"], None)
            action = create_action(widget, item["name"], method)
            menu_bar.addAction(action)
    return menu_bar
