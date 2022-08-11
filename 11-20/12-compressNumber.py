from itertools import groupby


#Variant One
def compress(number):
    results = []
    for key, group in groupby(str(number)):
        results.append((key, len(list(group))))
    
    return results

print(compress(1000115560))

#Variante two. List comprehension
def compressV2(number):
    return [(key, len(list(group))) for key, group in groupby(str(number))]

print(compressV2(1000115560))