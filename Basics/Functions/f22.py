def foo(a, b, **kwargs):
    legal_args = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    for key in kwargs:
        if key not in legal_args:
            print(f'invalid argument: {key} = {kwargs[key]}')
            return
    print('Ok')

    
foo(10, 20, c=10, f=20, i=30, k=40) #valid
foo(10, 20, c=10, r=30) #invalid
