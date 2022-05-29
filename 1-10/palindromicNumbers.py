def calculate():
    palindromes = []
    for i in range(100, 1000):
        holder = str(i)
        if holder == holder[::-1]:
            palindromes.append(i)

    return len(palindromes)

print(calculate())