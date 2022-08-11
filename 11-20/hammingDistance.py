from dis import dis
from pydoc import doc


u = [1, 1, 0, 0, 1, 0, 0]
v = [1, 0, 1, 1, 0, 0, 0]

def hammingDistance(u, v):
    if len(u) != len(v): 
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    
    return distance

print(hammingDistance(u, v))