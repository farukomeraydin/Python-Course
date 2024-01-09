s = input('Enter a 3 digit number:')
result = (ord(s[0]) - ord('0')) * 100 + (ord(s[1]) - ord('0')) * 10 + ord(s[2]) - ord('0')
print(result)
