full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"     
    if " " in name:
        return"The character name should not contain spaces" 

    for stat in (strength,intelligence,charisma):
        if not isinstance(stat,int):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat> 4:            
            return "All stats should be no more than 4"  

    if sum((strength,intelligence,charisma)) != 7:
        return "The character should start with 7 points"

    def stat_bar(stat, max_value = 10):
        return full_dot * stat + empty_dot * (max_value - stat)
    
    return (
        f"{name}\n"
        f"STR {stat_bar(strength)}\n"
        f"INT {stat_bar(intelligence)}\n"
        f"CHA {stat_bar(charisma)}"
    )
    
print(create_character("ren",4,2,1))