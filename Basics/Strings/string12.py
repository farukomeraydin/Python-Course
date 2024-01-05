s = 'ali, veli, selami, ayşe, fatma'
a = s.split(',')
print(a)

a = s.split(', ')
print(a)

a = s.split(' ')
print(a)

s = 'ali,,,veli,,,selami'
a = s.split(',')
print(a)

s = 'ali   veli   selami'
a = s.split(' ')
print(a)

s = 'ali   veli \t\t \t       selami'
a = s.split()
print(a)

s = 'ali, veli, selami'
a = s.split('xx')
print(a)

s = 'ali,,,veli,,,selami'
a = s.split(',', 2)
print(a)
