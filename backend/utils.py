def sanitize_str(string: str) -> str:
    new_string = ""
    for i in range(len(string)):
        if string[i] == "\'":
            new_string += "\\\'" # adds \' to the string
        elif string[i] == "\"":
            new_string += "\\\"" # adds \" to the string
        else:
            new_string += string[i]
    return new_string