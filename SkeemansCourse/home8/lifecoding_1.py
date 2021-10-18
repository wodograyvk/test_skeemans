def some_function(one, two, three=0):
    if one and two:
        return one + two
    elif one:
        return one ** 2
    elif two:
        return three ** 3
    elif three:
        return -1
    else:
        return
    return 228
print(some_function(0, 2, 3))
