import math

def isprime(a):
    if a % 2 == 0:
        return a == 2
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    return True

for i in range(2, 100):
    if isprime(i):
        print(i, end=' ')
