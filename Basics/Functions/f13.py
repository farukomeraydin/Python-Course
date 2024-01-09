def foo(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
foo(100, c=200, b=300) #valid
#foo(100, c=300, 400) #invalid
