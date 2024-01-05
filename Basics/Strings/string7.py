s = 'bugün hava çok güzel, evet evet hava güzel'

index = s.find('hava')
print(index)

index = s.find('yarın') #doesn't exist
print(index)

index = s.find('hava', 10) #search after index 10
print(index)

index = s.find('z', 10, 20) #search between 10-20 index
print(index)
