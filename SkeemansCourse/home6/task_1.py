words = ['rabbit', 'computer', 'laptop', 'mask', 'core', 'padding', 'puppy']

word = choice(WORDS)

word  = "rabbit"

lives = 7
guessed_letters = []

while True:
    for c in word:
        if c in guessed_letters:
            print(c,end= " ")
        else:
            print("_", end= " ")
    print()
    print(f'Lives {lives}')
    print(f'Guessed_letters {guessed_letters}')


    guess = input("Enter the letter: ")
    guessed_letters.append(guess)
    if guess in word:
        print("you guessed")
    else:
        lives -= 1
        print("you are wrong")

    if len(set(guessed_letters) & set(word)) == len(set(word)):
        print("You won. Word {word} is correct!")
        break
    elif lives == 0:
        print(f"Game over! You out of lives. The word was {word}")






