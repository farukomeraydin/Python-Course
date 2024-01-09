def foo(a, *args, **kwargs):
    print('a = {}, args = {}, kwargs = {}'.format(a, args, kwargs))

foo(10, 20, 30, 40, xx='ali', y=100)
foo(10, 20, 30, 40)
foo(100, (200, 300))
