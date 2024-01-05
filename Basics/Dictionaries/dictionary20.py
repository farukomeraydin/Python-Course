d = {10: 'ali', 20: 'veli'}

result = d.setdefault(20) #gives value
print(result)

result = d.setdefault(100, 'sacit') #it will create one
print(result)

print(d)
