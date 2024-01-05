fs = frozenset([1, 'ali', 'selami', 2])
s = {1, 'sibel', 10, 'veli'}

result = fs & s
print(result, type(result))

result = s & fs
print(result, type(result))
