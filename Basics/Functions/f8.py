def foo():
    print('foo')

def bar():
    print('bar')

def tar():
    print('tar')

a = [foo, bar, tar]

for i in range(len(a)):
    a[i]()

for f in a:
    f()
