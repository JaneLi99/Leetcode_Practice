def isLongPressedName(name, typed):
    i = 0
    for char in typed:
        if i < len(name) and name[i] == char:
            i += 1
        else:
            if i == 0 or name[i - 1] != char:
                return False
    return i == len(name)

if __name__ == '__main__':
    print(isLongPressedName(name = "alex", typed = "aaleex"))
    print(isLongPressedName(name = "saeed", typed = "ssaaedd"))
