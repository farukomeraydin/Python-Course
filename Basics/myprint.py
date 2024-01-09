def myprint(*objects, sep=' ', end='\n'):
    i = 0
    while i < len(objects):
        if i != 0:
            print(end=sep)
        print(objects[i], end='')
        i += 1
    print(end=end)
    
myprint(10, 20, 30)
myprint(10, 20, 30, sep='*')
myprint(10, 20, 30, sep='*', end='/')
