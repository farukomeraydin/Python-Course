def disp_range(start, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0
    
    for i in range(start, stop, step):
        print(i, end = ' ')
    print()

disp_range(10)
disp_range(10, 20)
disp_range(10, 20, 2)
