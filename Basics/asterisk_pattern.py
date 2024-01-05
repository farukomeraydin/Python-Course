n = int(input('Bir sayı giriniz:'))
i = 1
while i <= n:
    k = 0
    while k < i:
        print('*', end='')
        k += 1
    print()
    i += 1
