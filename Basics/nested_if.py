a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))

max_val = a if a > c else c if a > b else b if b > c else c
print(max_val)
