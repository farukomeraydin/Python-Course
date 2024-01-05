path = r'c:\windows\systems\test.dll'
index = path.rfind('\\')
fname = path[index + 1:]
print(fname)
