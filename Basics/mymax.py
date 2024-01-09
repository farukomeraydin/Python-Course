def mymax(*args):
    if len(args) == 1:
        if isinstance(args[0], (int, float, bool)):
            return args[0]
        iterable = args[0]
    else:
        iterable = args
        
    maxval = None
    for x in iterable:
        if maxval == None or x > maxval:
            maxval = x
            
    return maxval


a = [1, 6, 3, 2, 5]

result = mymax(a)
print(result)

result = mymax(4, 16, 2, 3)
print(result)

result = mymax(4)
print(result)
