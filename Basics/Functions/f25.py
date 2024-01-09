def foo(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
x = [10, 20, 30]
foo(*x)
foo(*'ali')
#foo(*'ankara') error
