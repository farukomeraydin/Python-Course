b = []
for _ in range(5):
    a = [0] * 5
    b.append(a)
print(b)
print()

b[0][0] = 10 #Only first element changes
print(b)


a = [[0] * 5]
b = a * 5
print(b)
print()
b[0][0] = 10 #First element of each list changes
print(b)
