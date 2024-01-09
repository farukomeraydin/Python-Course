n = int(input('Enter a number:'))
a = []
for i in range(n):
    row = [0] * n
    row[i] = 1
    a.append(row)
    
for row in a:
    for x in row:
        print(x, end = ' ')
    print()
