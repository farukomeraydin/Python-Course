a = [10 ,20 ,30, 40, 50]

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=' ')
print()
for x in a[::-1]:
    print(x, end=' ')
print()
for x in reversed(a):
    print(x, end=' ')
