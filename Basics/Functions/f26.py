def bar(a, b, *args):
    print(f'a = {a}, b = {b}, args = {args}')
    
x = [10, 20, 30, 40, 50]
bar(100, *x)
