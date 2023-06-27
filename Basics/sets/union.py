a = {10, 'ali', 20, 'veli', 'selami', 30}
b = {30,'veli', 'ayşe', 40, 20, 'fatma'}

c = a | b
print(c)

c = a.union(b)
print(c)

x = [10, 'ali', 100, 200, 'sibel']

c = a.union(x)
print(c)
