s = 'bugün  hava çok güzel'

result = s.index('çok')
print(result)

result = s.rindex('a')
k = s[result:]
print(k)

result = s.index('izmir') #exception
print(result)
