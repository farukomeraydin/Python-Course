a = int(input('int bir sayı giriniz:'))

count = 0
while a != 0:
    count += 1
    a //= 10
print(count)
