s = input('Enter a string:')
text =''
for ch in s:
    text += ch if ch.isalnum() else ' '

words = text.split()
print(words)
