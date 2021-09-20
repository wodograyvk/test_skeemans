def palindrome(word) :
    return word == word[::-1]

word = str(input( "wtite a word: "))
print(palindrome(word))

