import time

start = time.time()
i = 0
while i < 100_000_000:
    i += 1
stop = time.time()
print(stop - start)
