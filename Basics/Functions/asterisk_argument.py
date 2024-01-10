a = [10, 20, 30, 40, 50]

for i in range(len(a)):
    if i != 0:
        print(', ', end='')
    print(a[i], end= '')
print()
print(*a, sep=', ') #more practical
