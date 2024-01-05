n = int(input('Enter a number:'))

i = 2
flag = True
while i < n:
    if n % i == 0:
        flag = False
    i += 1
        
if flag:
    print('Prime number')
else:
    print('Not prime number')
