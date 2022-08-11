def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
            return True
        else:
            return True

print(is_prime(15))
