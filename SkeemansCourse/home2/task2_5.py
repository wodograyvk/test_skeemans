def fact(n):
    factorial = 1 # accumulator
    for i in range(1, n + 1) :
        factorial *= i
    return factorial


fact(5)
