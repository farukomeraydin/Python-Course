s = input('Enter a string:')

upper_count = 0
lower_count = 0
for ch in s:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
        
print(f'Capital letter number = {upper_count}')
print(f'Lower case letter number = {lower_count}')
