import random

def head_tail(n):
    head = 0
    tail = 0
    
    for _ in range(n):
        result = random.randint(0, 1)
        if result == 0:
            head += 1
        else:
            tail += 1
    return head / n, tail / n

head, tail = head_tail(10)
print(head, tail)

head, tail = head_tail(1000)
print(head, tail)

head, tail = head_tail(1_000_000)
print(head, tail)
