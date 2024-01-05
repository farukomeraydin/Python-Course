a = [10, 20, 30, 40, 50]
i = 0
while i < len(a):
    print(id(a[i]))
    i += 1
print()
for x in a:
    print(id(x))
