def text_style_choice():
    style = input("Style? [1 - bold_left / 2 - bold_center / 3 - normal_left / 4 - normal_center] ").strip()
    if style == "1":
        return {"action": "text", "style": "bold_left"}
    elif style == "2":
        return {"action": "text", "style": "bold_center"}
    elif style == "3":
        return {"action": "text", "style": "normal_left"}
    elif style == "4":
        return {"action": "text", "style": "normal_center"}
    else:
        print("Invalid style. Defaulting to normal_left.")
        return {"action": "text", "style": "normal_left"}

def ask_user_about_primitive(key, value):
    print(f"\nFound primitive field: {key} with value: {value}")
    choice = input("How to show? [0 - skip / 1 - text / 2 no title text] ").strip()
    if choice == "1":
        style_config = text_style_choice()
        style_config["show_title"] = "on"
        return style_config

    if choice == "2":
        style_config = text_style_choice()
        style_config["show_title"] = "off"
        return style_config

    return {"action": "skip"}

def ask_user_about_dict(key, value):
    print(f"\nFound dict: {key} with {len(value)} values")
    choice = input("How to show? [0 - skip / 1 - plot / 2 - table / 3 - text / no title text] ").strip()
    if choice == "1":
        if not all(isinstance(v, (int, float)) for v in value.values()):
            print("Invalid value. Cannot plot non-numeric values.")
            return ask_user_about_dict(key, value)
        type_map = {"1": "line", "2": "pie", "3": "bar"}
        plot_choice = input("Type? [1 - line / 2 - pie / 3 - bar] ").strip()
        plot_type = type_map.get(plot_choice, "line")
        return {"action": "plot", "type": plot_type, "title": key}
    elif choice == "2":
        return {"action": "table", "title": key}
    elif choice == "3":
        style_config = text_style_choice()
        style_config["show_title"] = "on"
        return style_config
    elif choice == "4":
        style_config = text_style_choice()
        style_config["show_title"] = "off"
        return style_config

    return {"action": "skip"}

def ask_user_about_list(key, value):
    print(f"\nFound list: {key} with {len(value)} values")

    if not value:
        print("List is empty. Skipping.")
        return {"action": "skip"}

    if all(isinstance(el, dict) for el in value):
        print("All elements are dicts")
        first_keys = set(value[0].keys())
        if all(set(el.keys()) == first_keys for el in value[1:]):
            print("All dicts have the same keys.")
            choice = input("Display as table? [1 - yes / 0 - skip] ").strip()
            if choice == "1":
                return {"action": "list_table"}
        else:
            print("Dicts have inconsistent keys.")
            return {"action": "skip"}

    elif all(isinstance(el, (str, int, float, bool)) for el in value):
        print("List of primitive values.")

    choice = input("Show as bullet list? [0 - skip / 1 - list] ").strip()
    if choice == "1":
        return {"action": "list"}
    return {"action": "skip"}

def analyze_json_structure(data):
    config = {}
    for key, value in data.items():
        if isinstance(value, (str, int, float, bool)):
            config[key] = ask_user_about_primitive(key, value)
        elif isinstance(value, dict):
            config[key] = ask_user_about_dict(key, value)
        elif isinstance(value, list):
            config[key] = ask_user_about_list(key, value)
        else:
            config[key] = {"action": "skip"}
    return config
