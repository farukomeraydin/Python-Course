import random

a = ['ali', 'veli', 'ayşe']

result = random.sample(a, 4, counts=[4, 3, 2]) #4 for ali, 3 for veli, 2 for ayşe and get 4 samples
print(result)
