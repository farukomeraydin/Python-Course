def add(*args):
    total = 0
    for x in args:
        if isinstance(x, (tuple, list)):
            total += add(*x)
        else:
            total += x
    return total

result = add(1, (2, (3,5)), (6,7))
print(result)
