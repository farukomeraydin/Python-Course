def add(*args):
    total = 0
    for x in args:
        total += x
    return total

result = add()
print(result)

result = add(10)
print(result)

result = add(10, 20, 30)
print(result)
