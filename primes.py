import time
from math import sqrt
time.perf_counter()

primes_up_to = 1000000

# Mark's solution
start = time.perf_counter()

list_of_primes=[2]

for x in range(2,primes_up_to):
    prime = True
    max = sqrt(x)
    for y in list_of_primes:
        if y > max:
            break
        if (x % y) == 0:
            prime = False
    if prime:
        list_of_primes.append(x)

print(len(list_of_primes))
finish = time.perf_counter()

elapsed_time = finish - start
print("Mark's elapsed time: ",elapsed_time)