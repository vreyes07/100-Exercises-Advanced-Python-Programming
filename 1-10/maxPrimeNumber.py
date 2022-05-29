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

    maximo = max(sequence)
        
    return maximo

print(calculate(13195))