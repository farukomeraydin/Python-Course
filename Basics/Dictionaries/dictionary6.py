d = {'ali':10, 'veli':20, 'selami':30, 'ayşe':40, 'fatma':50}
print(d)

val = d.get('selami', 'Not Found')
print(val)

val = d.get('sacit', 'Not Found')
print(val)

val = d.get('sacit')
print(val)
