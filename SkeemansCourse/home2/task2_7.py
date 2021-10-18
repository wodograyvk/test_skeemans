def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def first_prime_numbers(n):
    result = []
    current_number = 1
    while len(result) < n:
        if is_prime(current_number):
            result.append(current_number)
        current_number += 1

    return  result

print(first_prime_numbers(6))
