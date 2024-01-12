#test.py

import sys

sys.path.insert(0, r'C:\Users\Pc\Desktop')

print(sys.path)

import util

result = util.isprime(101)
print('prime' if result else 'not prime')



#util.py
import math

def isprime(val):
    if val % 2 == 0:
        return val == 2
    
    sqrt_val = math.sqrt(val)
    for i in range(3, int(sqrt_val) + 1):
        if val % i == 0:
            return False
        
    return True

if __name__ == '__main__': #when imported this block wont be executed
    for i in range(2, 1000):
        if isprime(i):
            print(i, end=' ')
