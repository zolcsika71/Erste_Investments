# tests/test_menu_config.py

from gui.menu_config import generate_menu_structure


def test_generate_menu_structure():
    menu_data = {
        "main_1": {
            "name": "Import Suggested Portfolio",
            "submenus": None
        },
        "main_2": {
            "name": "Display",
            "submenus": {
                "name_1": "Show Current Portfolio",
                "name_2": "Sell and Buy on Current Portfolio",
                "name_3": "Show Suggested Portfolio"
            }
        }
    }
    expected_structure = [
        {
            "name": "Import Suggested Portfolio",
            "action": "import_suggested_portfolio",
            "submenus": None
        },
        {
            "name": "Display",
            "action": "display",
            "submenus": [
                {
                    "name": "Show Current Portfolio",
                    "action": "show_current_portfolio"
                },
                {
                    "name": "Sell and Buy on Current Portfolio",
                    "action": "sell_and_buy_on_current_portfolio"
                },
                {
                    "name": "Show Suggested Portfolio",
                    "action": "show_suggested_portfolio"
                }
            ]
        },
        {
            "name": "Exit",
            "action": "exit",
            "submenus": None
        }
    ]
    assert generate_menu_structure(menu_data) == expected_structure
