def foo(a, b, *c):
    print(f'a = {a}, b = {b}, c = {c}')
    
foo(10, 20, 30, 40, 50, 60)
foo(10, 20, 30)
foo(10, 20)
