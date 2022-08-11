def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]


#Variant one
def calculate():
    palindromes = []
    for i in range(100, 1000):
        if is_palindrome(i):
            palindromes.append(i)

    return palindromes

print(calculate())

#Variant two. List comprehension
def calculateV2():
    return [i for i in range(100, 1000) if is_palindrome(i)]

print(calculateV2())