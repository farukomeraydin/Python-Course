def foo(a, *b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
#foo(10, 20, 30) #error
foo(10, 20, c=30)
