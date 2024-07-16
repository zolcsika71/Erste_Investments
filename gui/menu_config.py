# gui/menu_config.py

from .menu_constants import menu as menu_constants


def convert_to_function(name):
    """Convert a name to its corresponding action."""
    return name.lower().replace(" ", "_")


def generate_menu_structure(menu_data):
    menu_mapping = []
    for main_key, main_value in menu_data.items():
        main_menu_item = {
            "name": main_value["name"],
            "action": convert_to_function(main_value["name"]),
            "submenus": []
        }
        if main_value["submenus"]:
            submenus = []
            for sub_key, sub_value in main_value["submenus"].items():
                submenu_item = {
                    "name": sub_value,
                    "action": convert_to_function(sub_value)
                }
                submenus.append(submenu_item)
            main_menu_item["submenus"] = submenus
        else:
            main_menu_item["submenus"] = None
        menu_mapping.append(main_menu_item)

    # Ensure Exit menu item is included
    exit_menu_item = {
        "name": "Exit",
        "action": "exit",
        "submenus": None
    }
    menu_mapping.append(exit_menu_item)

    return menu_mapping


menu_structure = generate_menu_structure(menu_constants)
