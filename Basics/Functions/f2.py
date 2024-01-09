def foo():
    a = int(input('Bir değer giriniz:'))
    if a > 0:
        return a * a
    return 'error'

result = foo()
print(result, type(result))
