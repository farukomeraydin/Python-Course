a = 10
b = 20
c = 30
s = 'a = {0}, b = {1}, c = {2}'
k = s.format(a, b, c)
print(k)

s = '{2} {0} {1}'
k = s.format(a, b, c)
print(k)

print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
print('{2} {2} {1} {0} {1}'.format(a, b, c))
