test_settings = {
    "language": "en", 
    "notifications": True
}

def add_setting(test_settings,new_option):
    key,value = new_option
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        test_settings[key] = value
        return (f"Setting '{key}' added with value '{value}' successfully!")



def update_setting(test_settings,upd_option):
    key,value = upd_option
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        test_settings[key] = value
        return (f"Setting '{key}' updated to '{value}' successfully!")
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")



def delete_setting(test_settings,del_option):
    key = del_option
    key = key.lower()
    if key in test_settings:
       del test_settings[key]
       return (f"Setting '{key}' deleted successfully!")
    else:
        return("Setting not found!")




def view_settings(settings):
    
    if not settings:
        return "No settings available."
     

    lines = ["Current User Settings:"]

    for k,v in settings.items():
        capitalized_key = k[0].upper() + k[1:]

        lines.append(f"{capitalized_key}: {v}")

    return "\n".join(lines) + "\n"


print(view_settings(test_settings))
add_setting(test_settings,("volume","Up"))

#code works with strings. if provided tuple with value type of int things break. Need to modify so everything works with integers as well. 