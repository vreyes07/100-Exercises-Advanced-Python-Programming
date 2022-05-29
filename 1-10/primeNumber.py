from ast import Num


def calculate(number):
    pivot = 2
    sequence = []
    while pivot * pivot <= number:
        if not number % pivot == 0:
            pivot += 1
        else:
            number = number // pivot
            sequence.append(pivot)

    if number > 1:
        sequence.append(number)
        
    return sequence

print(calculate(48))

'''
def calculate2(number):
    i = 2
    factors = []
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

print(calculate2(48))
'''