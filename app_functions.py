# app_functions.py

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
