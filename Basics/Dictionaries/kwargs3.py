def foo(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
d = {'b': 'ankara', 'c': 12.3}

foo(100, **d)
