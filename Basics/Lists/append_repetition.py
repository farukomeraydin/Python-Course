a = [[]]
b = a * 3 # [[]] + [[]] + [[]]
print(b)
b[0].append(100) #We assign address
print(b)
b[1].append(200)
print(b)
