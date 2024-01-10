def foo(a, b, c, d, e, f):
    print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}')
    
t = (10, 20)
d = {'d':10, 'e':20}

foo(1, 2, 3, f=10, *t)
foo(1, 2, f=10, *t, e=30)
foo(1, 2, f=10, **d, c=200)
