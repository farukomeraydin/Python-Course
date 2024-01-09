def myprint(*objects, sep=' ', end='\n'):
    if len(objects):
        print(objects[0], end='')
    for x in objects:
        print(end=sep)
        print(x, end='')
    print(end=end)
        
        
myprint(10, 20, 30)
myprint(10, 20, 30, sep='*')
myprint(10, 20, 30, sep='*', end='/')
