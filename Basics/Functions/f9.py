def foo():
    print('foo')

def bar():
    print('bar')

def tar():
    print('tar')

d = {'ali': foo, 'veli': bar, 'selami': tar}
d['ali']()
d['veli']()
d['selami']()
