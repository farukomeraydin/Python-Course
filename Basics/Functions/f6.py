def foo():
    a = 10
    print(id(a))
    return a

result = foo()
print(id(result))
