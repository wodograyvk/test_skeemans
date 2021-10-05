number = input ("Какое число считаем победным?: ")
print(number)

from random import randint
repeat = True
while repeat:
    print("You rolled",randint(1,6))
    print('Do yoy want to roll again? Y/N')
    repeat = ("y" or "yes") in input().lower()
