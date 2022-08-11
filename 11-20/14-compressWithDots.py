from itertools import groupby

def compress(number):
    results = []

    for key, group in groupby(str(number)):
        #results.append(key)
        results.append(str(key)+str('.'*len(list(group))))
        results = [''.join(item) for item in results]
    
    return ''.join(results)

print(compress(1000115560))