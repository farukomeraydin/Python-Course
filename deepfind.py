a = [3, 6, 1, [34, 51, [11, 32, 34]], 23, 10]

def deepfind(a, val):
    for x in a:
        if isinstance(x, list):
            if deepfind(x, val):
                return True
        else:
            if x == val:
                return True
    return False

result = deepfind(a, 34)
print(result)
