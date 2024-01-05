s = '  \t      ankara \t       '
k = s.strip()
print(k)

s='xxxxxxankaraxxxxxxxxx'
k = s.strip('x')
print(k)

s='xxxyyyyxxzxankaraxxzxxxyyyyxxxx'
k = s.strip('xyz')
print(k)
