s = 'ankaraizmiristanbul'
left, center, right = s.partition('izmir')
print(left)
print(center)
print(right)

s = 'ankaraizmiristanbul'
t = s.partition('xxx')
print(t)

t = s.partition('ankara')
print(t)

t = s.partition('istanbul')
print(t)
