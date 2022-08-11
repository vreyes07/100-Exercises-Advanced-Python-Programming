#Implement a function that returns the largest palindrome number resulting from the product of two-digits number

def calculate():
    palindromes = []
    for i in range(10, 100):
        for j in range(10, 100):
            if str(i * j) == str(i * j)[::-1]:
                palindromes.append(i * j) 

    return max(palindromes)

print(calculate())