def foo(a, b, /, c, *, d, e):
    print(a, b, c, d, e)
    
foo(10, 20, 30, d=40, e=50)
foo(10, 20, c=30, d=40, e=50)
