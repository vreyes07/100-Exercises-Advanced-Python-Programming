def greatest_common_divisor(a, b):
    holder = max(a, b)
    common_divisors = []
    for i in range(1, holder):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)

    return max(common_divisors)

print(greatest_common_divisor(64, 32))