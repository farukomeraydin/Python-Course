a = {10, 'ali', 20, 'veli', 'selami', 30}
b = {30,'veli', 'ayşe', 40, 20, 'fatma'}

c = a ^ b
print(c)

c = a.symmetric_difference(b)
print(c)

x = 'ali', 10, 20, 'ayşe'
c = a.symmetric_difference(x)
print(c)
