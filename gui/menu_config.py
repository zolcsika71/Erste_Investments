# menu_config.py

menu_structure = [
    {
        "name": "Import Suggested Portfolio",
        "action": "import_suggested_portfolio",
        "method_name": "import_suggested_portfolio",
        "menu": None,
    },
    {
        "name": "Display",
        "submenus": [
            {
                "name": "Show Current Portfolio",
                "action": "show_current_portfolio",
                "method_name": "show_current_portfolio",
            },
            {
                "name": "Sell and Buy on Current Portfolio",
                "action": "sell_buy_on_current_portfolio",
                "method_name": "sell_buy_on_current_portfolio",
            },
            {
                "name": "Show Suggested Portfolio",
                "action": "show_suggested_portfolio",
                "method_name": "show_suggested_portfolio",
            },
        ],
    },
    {
        "name": "Service",
        "submenus": [
            {
                "name": "Delete and Recreate DB",
                "action": "delete_and_recreate_db",
                "method_name": "delete_recreate_db",
            },
            {
                "name": "Import Current Portfolio",
                "action": "import_current_portfolio",
                "method_name": "import_current_portfolio",
            },
        ],
    },
    {"name": "Exit", "action": "exit", "method_name": "confirm_exit", "menu": None},
]
