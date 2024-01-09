s = input('Enter a string:')
delimiters = '\t!,.-\'"+()*{}[] '
print(delimiters)

words = []
i = 0
while True:
    while i < len(s) and s[i] in delimiters:
        i += 1
    if i == len(s):
        break
    start = i
    while i < len(s) and not s[i] in delimiters:
        i += 1
    word = s[start:i]
    words.append(word)
print(words)
