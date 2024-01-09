def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(10, 20, c=30, d=40)
foo(10, 20, d=30, c=40)
