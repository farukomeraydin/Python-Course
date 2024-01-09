def foo(a, b, c, *d):
    print(f'a = {a}, b = {b}, c = {c}, d = {d}')
    
foo(100, *range(10))
