from itertools import groupby

def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)

def decompress(regexc):
    holder = [tuple(item) for item in regexc.split('_')]
    result = [i * int(j) for i, j in holder]
    return int(''.join(result))