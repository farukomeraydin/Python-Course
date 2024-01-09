a = [10, 20, 30, 40, 50, 60]
temp = a[:len(a) // 2]

a[:len(a) // 2] = a[len(a) // 2 + len(a) % 2:]
a[len(a) // 2 + len(a) % 2:] = temp

print(a)
