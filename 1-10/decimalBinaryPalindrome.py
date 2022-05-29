def is_palindrome(number):
    binary = bin(number)[2:]
    #while number // 2 != 0:
    if str(number) == str(number)[::-1] and str(binary) == str(binary)[::-1]:
        print(f'binary original:  {binary}, binary: {binary[::-1]}')
        return True
    else:
        return False

print(is_palindrome(99))