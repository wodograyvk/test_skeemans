def print_stars(height) :
    for i in range(height) :
        for i in range(i + 1) :
            print("*", end=(" "))
        print()

    for i in range(height, 0, -1) :
        for i in range(i, 1, -1) :
            print("*", end=(" "))
        print()

height = int(input("input height jf triangle: "))
print_stars(height)
print_stars(height)
print_stars(height)

