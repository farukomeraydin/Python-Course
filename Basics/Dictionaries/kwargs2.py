def foo(a, b, c, d=100):
    print(f'a = {a}, b = {b}, c = {c}, d = {d}')
    
d = {'a': 10, 'b': 'ankara', 'c': 12.3}

foo(**d)
