def foo(a, b, **kwargs):
    legal_args = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    for key in kwargs:
        if key not in legal_args:
            print(f'invalid argument: {key} = {kwargs[key]}')
            return
    c = kwargs.get('c', 100)
    d = kwargs.get('d', 200)
    e = kwargs.get('e', 300)
    f = kwargs.get('f', 400)
    g = kwargs.get('g', 500)
    h = kwargs.get('h', 600)
    i = kwargs.get('i', 700)
    j = kwargs.get('j', 800)
    k = kwargs.get('k', 900)
    l = kwargs.get('l', 1000)
    m = kwargs.get('m', 1100)
    
    print(f'c = {c}, d = {d}, e = {e}, f = {f}, g = {g}, h = {h}, i = {i}, j = {j}, k = {k}, l = {l}, m = {m}')

    
foo(10, 20, c=10, f=20, i=30, k=40)
foo(10, 20)
