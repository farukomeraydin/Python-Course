a = [1,2,3,4,5]
print(a)
b = a.copy()
a[0] = 100 #b is not affected same as b=a[:]
print(b)
