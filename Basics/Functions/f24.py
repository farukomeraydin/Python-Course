def foo(a, b, **kwargs):
    legal_args = {'c': 100, 'd': 200, 'e': 300, 'f': 400, 'g': 500, 'h': 600, 'i': 700, 'j': 800, 'k': 900, 'l': 1000, 'm': 1100}
    
    for key, value in kwargs.items():
        if key not in legal_args:
            print(f'invalid argument: {key} = {kwargs[key]}')
            return
        else:
            legal_args[key] = value

    for key, value in legal_args.items():
        print(f'parameter:{key}, value: {value}')

    
foo(10, 20, c=10, f=20, i=30, k=40)
print()
foo(10, 20)
