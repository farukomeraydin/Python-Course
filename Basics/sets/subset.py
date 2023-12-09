a = {10, 20, 30, 40, 50}
b = {10, 40}
result = b < a
print(result)

result = a < a #self subset
print(result)

result = a <= a #subset
print(result)

result = a > b #superset
print(result)

result = a.issubset(range(10, 100, 10))
print(result)
