def foo(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
d = {'a': 10, 'b': 'ankara', 'c': 12.3}

foo(**d)
