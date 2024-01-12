s = input('Enter a string:')
d = {}

for ch in set(s):
    d[ch] = s.count(ch)
print(d)
