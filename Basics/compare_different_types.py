a = [10, 20]
b = (10, 20)

result = a == b #Always False
print(result)

result = a != b #Always True
print(result)


a = [1, [2, 3, 4], 5]
b = [1, (2, 3, 4), 2]
result = a == b
print(result)
