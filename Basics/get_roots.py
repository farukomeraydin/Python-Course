import math
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print('kök yok')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f'x1 = {x1}, x2 = {x2}')
