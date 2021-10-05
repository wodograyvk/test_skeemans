while 1 == 1:
    import random

    input("Иогрок 1, введите число, которое будем считать победным. \n От 1 до 6")
    answer = input()
    print("Хорошо, твое число " + str (answer))

    input("Иогрок1, нажмит enter, чтобы бросить кости")
    player1 = random.randint(1,6)
    print(player1)

    input("Хорошо, я ввожу число, которое буду считать победным. \n Тоже от 1 до 6")
    player2 = random.randint(1,6)
    print(player2)

    if player1 > player2:
        print("Поздравляю! Ты победил!")
    elif player1 == player2:
        print("Выходит ничья")
    else:
        print("Пускай сегодня не повезло. Но сдаваться рано!")

    igra = input("Хочешь сыграть еще? Тогда введи y. Если не хочешь, введи n: ")
    if igra == "n":
        break
    elif igra == "y":
        pass