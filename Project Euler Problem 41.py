#Problem 41
#https://projecteuler.net/problem=41
#What is the largest n-digit pandigital prime that exists

from sieve_of_era import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(10000000)
largest_pan_prime = 0

def check_pandigital(f):
  g = set(str(f))
  check = set([str(n) for n in range(1,len(str(f))+1)])
  if g == check and len(g) == len(str(f)):
    return True
  else:
    return False

for p in primes:
  if check_pandigital(p):
    largest_pan_prime = max(largest_pan_prime, p)

print(largest_pan_prime)