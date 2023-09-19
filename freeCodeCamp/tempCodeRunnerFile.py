def replace_word():
    replace_with = ["chief", "thief", "superintendent",
                    "sweeper", "married", "left", "tried", "died"]
    s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
    index = 0
    while index < len(replace_with):
        if replace_with[index] in string:
            if index != len(replace_with)-1:
                string = string.replace(
                    replace_with[index], replace_with[index+1])
        index += 2

    print(string)


replace_word()
