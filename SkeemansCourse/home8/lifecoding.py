def my_map(func, col):
    for i in col:
        yield func(i)

for i in my_map(lambda x:x ** 2, range(10)):

    print(i)



