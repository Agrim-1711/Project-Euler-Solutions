#Problem 35
#https://projecteuler.net/problem=35
#How many circular primes are there below one million?

from sieve_of_era import sieve_of_eratosthenes
from rotation import rotation

primes = (sieve_of_eratosthenes(1000000))

to_flag = [0,2,4,5,6,8]
to_remove = [2,5] # 2 and 5 are 1-digit primes

for p in primes:
  q = list(str(p))
  for r in to_flag:
    if str(r) in q:
      to_remove.append(p)

for r in to_remove:
  if r in primes:
    primes.remove(r)

set_primes = set(primes)
circular = []

for x in primes:
  y = set(rotation(x))
  if set_primes.intersection(y) == y:
    circular.append(x)

print(len(circular))